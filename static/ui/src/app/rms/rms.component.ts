import {Component, OnInit} from '@angular/core';
import {FormGroup, FormBuilder, Validators} from "@angular/forms";
import {ProsesService} from "../services/proses.service";

declare let Plotly;

@Component({
    selector: 'ui-rms',
    templateUrl: './rms.component.html',
    styleUrls: ['./rms.component.css']
})
export class RmsComponent implements OnInit {
    rmsForm: FormGroup;
    title: string;
    deskripsi: string;
    data: any;
    layout: any;
    data_rms: any;
    private isShow: boolean = false;

    constructor(private fb: FormBuilder,
                private rms: ProsesService) {
    }

    ngOnInit() {
        this.title = 'Grafik RMS Angin';
        this.deskripsi = 'Grafik yang digunakan untuk menampilkan RMS data angin.';
        this.createWindroseForm();
    }

    createWindroseForm() {
        this.rmsForm = this.fb.group({
            v_max: this.fb.control('', Validators.required),
            v_step: this.fb.control('', Validators.required),
            arah: this.fb.control('', Validators.required),
        });
    }

    onFormRMSSubmit(obj) {
        let vmax = obj['v_max'];
        let step = obj['v_step'];
        let arah = obj['arah'];

        this.isShow = true;
        this.rms.ambilRMSAngin(vmax, step, arah).subscribe(
            val => {
                this.data_rms = val[0];
                this.isShow = false;

                let trace = {
                    x: this.data_rms['x'],
                    y: this.data_rms['y'],
                    fill: 'tonexty',
                    type: 'scatter'
                };

                this.layout = {
                    title: 'Grafik RMS',
                    xaxis: {
                        title: 'Rentang Kecepatan [m/s]'
                    },
                    yaxis: {
                        title: 'RMS Getaran'
                    }
                };

                this.data = [trace];

                Plotly.newPlot('plotRMS', this.data, this.layout);
            }
        );
    }
}
