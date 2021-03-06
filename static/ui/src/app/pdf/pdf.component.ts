import {Component, OnInit} from '@angular/core';
import {FormGroup, FormBuilder, Validators} from "@angular/forms";
import {ProsesService} from "../services/proses.service";
import {IMyOptions} from "mydatepicker";

declare let Plotly: any;

@Component({
    selector: 'ui-pdf',
    templateUrl: './pdf.component.html',
    styleUrls: ['./pdf.component.css']
})
export class PdfComponent implements OnInit {
    title: string;
    deskripsi: string;
    pdfForm: FormGroup;
    isShow: boolean = false;
    isError: boolean;
    key: any;
    message: any;

    private data: any;
    private layout: any;
    private data_angin: any;
    private myDatePickerOptions: IMyOptions;

    constructor(private fb: FormBuilder,
                private proses: ProsesService) {
    }

    ngOnInit() {
        this.title = 'Grafik PDF Kecepatan Angin';
        this.deskripsi = 'Grafik Probability Density Function untuk kecepatan angin';
        this.myDatePickerOptions = {
            dateFormat: 'yyyy-mm-dd',
        };
        this.createFormAngin({});
    }

    createFormAngin(data) {
        this.pdfForm = this.fb.group({
            date_from: this.fb.control(data.date_from, Validators.compose([Validators.required])),
            date_to: this.fb.control(data.date_to, Validators.compose([Validators.required])),
        });
    }

    onFormAnginSubmit(val) {
        this.isShow = true;
        this.proses.ambilPdfAngin(val['date_from']['formatted'], val['date_to']['formatted']).subscribe(
            obj => {
                this.data_angin = obj[0];

                this.layout = {
                    title: `Grafik PDF Kecepatan Angin <br> Mean: ${this.data_angin['mean']} | Std: ${this.data_angin['std']}`,
                    xaxis: {
                        title: 'Kecepatan [m/s]'
                    },
                    yaxis: {
                        title: 'Probability Density'
                    },
                    legend: {font: {size: 16}},
                };

                let trace1 = {
                    x: this.data_angin['kecepatan_x'],
                    type: 'histogram',
                    histnorm: 'probability density',
                    name: 'Hist. Angin'
                };

                let trace2 = {
                    x: this.data_angin['kecepatan_x'],
                    y: this.data_angin['kecepatan_y'],
                    name: 'Fitting normal',
                    marker: {color: '#db2828'},
                    type: 'scatter'
                };

                this.data = [trace1, trace2];

                Plotly.newPlot('plotPdf', this.data, this.layout);
                this.isShow = false;
            },
            err => {
                this.isShow = false;
                this.isError = true;
                this.key = Object.keys(err);
                this.message = err;
            }
        );
    }
}
