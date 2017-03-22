import {Component, OnInit} from '@angular/core';
import {FormGroup, Validators, FormBuilder} from "@angular/forms";
import {ProsesService} from "../services/proses.service";

declare let Plotly;

@Component({
    selector: 'ui-waterfall',
    templateUrl: './waterfall.component.html',
    styleUrls: ['./waterfall.component.css']
})
export class WaterfallComponent implements OnInit {
    waterfallForm: FormGroup;
    title: string;
    deskripsi: string;
    data: any;
    layout: any;
    data_waterfall: any;
    private isShow: boolean = false;

    constructor(private fb: FormBuilder,
                private waterfall: ProsesService) {
    }

    ngOnInit() {
        this.title = 'Grafik Waterfall Getaran';
        this.deskripsi = 'Besaran Frekuensi, kecepatan angin, dan amplitudo getaran dalam grafik 3D.';
        this.createWaterfallForm();
    }

    createWaterfallForm() {
        this.waterfallForm = this.fb.group({
            date_from: this.fb.control('', Validators.required),
            date_to: this.fb.control('', Validators.required),
            v_max: this.fb.control('', Validators.required),
            v_step: this.fb.control('', Validators.required),
            arah: this.fb.control('', Validators.required),
            wkt_awal: this.fb.control(''),
            wkt_akhir: this.fb.control(''),
            simplified: this.fb.control(true),
        });
    }

    onFormWaterfallSubmit(obj) {
        let date_from = obj['date_from'];
        let date_to = obj['date_to'];
        let vmax = obj['v_max'];
        let step = obj['v_step'];
        let arah = obj['arah'];
        let wkt_awal = obj['wkt_awal'];
        let wkt_akhir = obj['wkt_akhir'];
        let simplified = obj['simplified'];

        this.isShow = true;
        this.waterfall.ambilWaterfallAngin(date_from, date_to,
            vmax, step, arah,
            wkt_awal, wkt_akhir, simplified).subscribe(
            val => {
                this.data = [];
                this.data_waterfall = val[0];
                this.data_waterfall['x'].forEach(
                    (v, k) => {
                        this.data.push(
                            {
                                x: this.data_waterfall['x'][k],
                                y: this.data_waterfall['y'][k],
                                z: this.data_waterfall['z'][k],
                                name: `Group V - ${k}`,
                                mode: 'lines',
                                type: 'scatter3d',
                                line: {
                                    width: 3,
                                    colorscale: "Viridis"
                                }
                            }
                        );
                    }
                );

                this.layout = {
                    title: 'Grafik Getaran',
                    showlegend: false,
                    height: 690,
                    margin: {
                        l: 0,
                        r: 0,
                        b: 0,
                        t: 25
                    },
                    scene: {
                        camera: {
                            eye: {
                                x: -3.5,
                                y: -2.8,
                                z: -0.1
                            }
                        },
                        aspectmode: 'manual',
                        aspectratio: {
                            x: 1.5,
                            y: 3,
                            z: 2
                        },
                        xaxis: {
                            title: 'x = Kec [m/s]',
                            titlefont: {
                                color: '#FF6138',
                                family: 'Arial, Open Sans',
                                size: 11
                            }
                        },
                        yaxis: {
                            title: 'y = Frek [Hz]',
                            titlefont: {
                                color: '#FF6138',
                                family: 'Arial, Open Sans',
                                size: 11
                            }
                        },
                        zaxis: {
                            title: 'z = Aplitd [m/s2]',
                            titlefont: {
                                color: '#FF6138',
                                family: 'Arial, Open Sans',
                                size: 11
                            }
                        }
                    }
                };
                Plotly.newPlot('plotWaterfall', this.data, this.layout);
                this.isShow = false;
            }
        );
    }
}
