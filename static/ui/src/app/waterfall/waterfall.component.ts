import {Component, OnInit} from '@angular/core';
import {FormGroup, Validators, FormBuilder} from "@angular/forms";
import {ProsesService} from "../services/proses.service";
import {IMyOptions} from "mydatepicker";

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
    private isError: boolean;
    key: any;
    message: any;
    private isSimplified: boolean = true;
    private myDatePickerOptions: IMyOptions;

    constructor(private fb: FormBuilder,
                private waterfall: ProsesService) {
    }

    ngOnInit() {
        this.title = 'Grafik Waterfall Getaran';
        this.deskripsi = 'Besaran Frekuensi, kecepatan angin, dan amplitudo getaran dalam grafik 3D.';
        this.myDatePickerOptions = {
            dateFormat: 'yyyy-mm-dd',
        };
        this.createWaterfallForm();
    }

    createWaterfallForm() {
        let cekBox = this.fb.control(this.isSimplified);
        let rentang = this.fb.control({value: '', disabled: this.isSimplified});
        let max = this.fb.control({value: '', disabled: this.isSimplified});
        let wkt_awal = this.fb.control({value: '', disabled: this.isSimplified});
        let wkt_akhir = this.fb.control({value: '', disabled: this.isSimplified});

        this.waterfallForm = this.fb.group({
            date_from: this.fb.control('', Validators.required),
            date_to: this.fb.control('', Validators.required),
            v_max: max,
            v_step: rentang,
            arah: this.fb.control('', Validators.required),
            wkt_awal: wkt_awal,
            wkt_akhir: wkt_akhir,
            simplified: cekBox,
        });

        cekBox.valueChanges.subscribe(
            val => {
                if (val) {
                    max.disable();
                    rentang.disable();
                    wkt_awal.disable();
                    wkt_akhir.disable();
                }
                else {
                    max.setValidators(Validators.required);
                    rentang.setValidators(Validators.required);
                    max.enable();
                    rentang.enable();
                    wkt_awal.enable();
                    wkt_akhir.enable();
                }
            }
        );
    }

    onFormWaterfallSubmit(obj) {
        let date_from = obj['date_from']['formatted'];
        let date_to = obj['date_to']['formatted'];
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
