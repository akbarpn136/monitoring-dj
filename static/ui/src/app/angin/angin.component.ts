import {Component, OnInit} from '@angular/core';
import {FormBuilder, Validators, FormGroup} from "@angular/forms";
import {ProsesService} from "../services/proses.service";

declare let Plotly: any;

@Component({
    selector: 'ui-angin',
    templateUrl: './angin.component.html',
    styleUrls: ['./angin.component.css']
})
export class AnginComponent implements OnInit {
    title: string;
    deskripsi: string;
    anginForm: FormGroup;

    private data: any;
    private options: any;
    private layout: any;
    private data_angin: any;

    constructor(private fb: FormBuilder,
                private proses: ProsesService) {
    }

    ngOnInit() {
        this.createFormAngin({});
    }

    createFormAngin(data) {
        this.title = 'Grafik Distribusi';
        this.deskripsi = 'Grafik perubahan kecepatan angin terhadap waktu untuk arah angin yang ditentukan beserta getaran';

        this.anginForm = this.fb.group({
            date_from: this.fb.control(data.date_from, Validators.compose([Validators.required])),
            date_to: this.fb.control(data.date_to, Validators.compose([Validators.required])),
            jenis: this.fb.control(data.jenis, Validators.compose([Validators.required])),
        });
    }

    onFormAnginSubmit(val) {
        this.proses.ambilAtributAngin(val['date_from'], val['date_to']).subscribe(
            obj => {
                this.data_angin = obj;

                let key_x: any[] = [];
                let key_y: any[] = [];
                this.data_angin.forEach(
                    v => {
                        key_x.push(`${v['tanggal']} ${v['waktu']}`);
                        if (val['jenis'] === 'kecepatan') {
                            key_y.push(v['kecepatan']);
                        }
                        else if (val['jenis'] === 'arah') {
                            key_y.push(v['arah']);
                        }
                        else {
                            key_y.push(v['akselerator5']);
                        }
                    }
                );

                let trace1 = {
                    x: key_x,
                    y: key_y,
                    mode: 'line',
                    connectgaps: false
                };

                if (val['jenis'] === 'kecepatan') {
                    this.layout = {
                        title: 'Grafik Kecepatan Angin',
                        xaxis: {
                            title: 'Waktu'
                        },
                        yaxis: {
                            title: 'Kecepatan [m/s]'
                        }
                    };
                }

                else if (val['jenis'] === 'arah') {
                    this.layout = {
                        title: 'Grafik Arah Angin',
                        xaxis: {
                            title: 'Waktu'
                        },
                        yaxis: {
                            title: 'Arah [derajat]'
                        }
                    };
                }

                else {
                    this.layout = {
                        title: 'Grafik Getaran oleh Angin',
                        xaxis: {
                            title: 'Waktu'
                        },
                        yaxis: {
                            title: 'Akselerasi [m/s2]'
                        }
                    };
                }

                this.data = [trace1];

                Plotly.newPlot('plotAngin', this.data, this.layout);
            }
        );
    }
}
