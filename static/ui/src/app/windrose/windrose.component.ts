import {Component, OnInit} from '@angular/core';
import {FormGroup, FormBuilder, Validators} from "@angular/forms";
import {ProsesService} from "../services/proses.service";

declare let Plotly;

@Component({
    selector: 'ui-windrose',
    templateUrl: './windrose.component.html',
    styleUrls: ['./windrose.component.css']
})
export class WindroseComponent implements OnInit {
    windroseForm: FormGroup;
    title: string;
    deskripsi: string;
    data: any;
    layout: any;
    data_windrose: any;
    private isShow: boolean = false;

    constructor(private fb: FormBuilder,
                private windrose: ProsesService) {
    }

    ngOnInit() {
        this.title = 'Grafik Windrose Angin';
        this.deskripsi = 'Persentase kecepatan angin dalam beberapa arah.';
        this.createWindroseForm();
    }

    createWindroseForm() {
        this.windroseForm = this.fb.group({
            date_from: this.fb.control('', Validators.required),
            date_to: this.fb.control('', Validators.required),
            v_max: this.fb.control('', Validators.required),
            v_step: this.fb.control('', Validators.required),
        });
    }

    onFormWindroseSubmit(obj) {
        let date_from = obj['date_from'];
        let date_to = obj['date_to'];
        let vmax = obj['v_max'];
        let step = obj['v_step'];

        this.isShow = true;
        this.windrose.ambilWindroseAngin(date_from, date_to, vmax, step).subscribe(
            val => {
                this.data_windrose = val;
                this.isShow = false;
                this.data = [];

                this.data_windrose.forEach(
                    data => {
                        let kompas = data['kompas'];
                        let nama = data['nama'];
                        let persentase = data['persentase'];
                        let trace = {
                            r: persentase,
                            t: kompas,
                            name: nama,
                            type: 'area'
                        };

                        this.data.push(trace);
                    }
                );

                this.layout = {
                    title: 'Wind Rose Angin',
                    font: {size: 16},
                    legend: {font: {size: 16}},
                    radialaxis: {ticksuffix: '%'},
                    orientation: 270,
                    margin: {r: 0}
                };

                Plotly.newPlot('plotWindrose', this.data, this.layout);
            }
        );
    }
}
