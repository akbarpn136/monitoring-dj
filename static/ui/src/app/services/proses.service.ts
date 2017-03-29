import {Injectable} from '@angular/core';
import {Http, Response, Headers, RequestOptions, URLSearchParams} from "@angular/http";

import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import {Observable} from "rxjs";
import {environment} from "../../environments/environment";

@Injectable()
export class ProsesService {
    private URL_ANGIN: string;
    private URL_WINDROSE: string;
    private URL_RMS: string;
    private URL_WATERFALL: string;
    private URL_PDF: string;

    constructor(private http: Http) {
        switch (environment.envName) {
            case 'dev':
                this.URL_ANGIN = 'http://localhost:8000/v1/monitor/angin/';
                this.URL_WINDROSE = 'http://localhost:8000/v1/monitor/windrose/';
                this.URL_RMS = 'http://localhost:8000/v1/monitor/rms/';
                this.URL_WATERFALL = 'http://localhost:8000/v1/monitor/waterfall/';
                this.URL_PDF = 'http://localhost:8000/v1/monitor/pdf/';
                break;

            case 'prod':
                this.URL_ANGIN = 'http://monitoring.bbta3.bppt.go.id/v1/monitor/angin/';
                this.URL_WINDROSE = 'http://monitoring.bbta3.bppt.go.id/v1/monitor/windrose/';
                this.URL_RMS = 'http://monitoring.bbta3.bppt.go.id/v1/monitor/rms/';
                this.URL_WATERFALL = 'http://monitoring.bbta3.bppt.go.id/v1/monitor/waterfall/';
                this.URL_PDF = 'http://monitoring.bbta3.bppt.go.id/v1/monitor/pdf/';
                break;

            case 'native':
                this.URL_ANGIN = 'http://monitoring.bbta3.bppt.go.id/v1/monitor/angin/';
                this.URL_WINDROSE = 'http://monitoring.bbta3.bppt.go.id/v1/monitor/windrose/';
                this.URL_RMS = 'http://monitoring.bbta3.bppt.go.id/v1/monitor/rms/';
                this.URL_WATERFALL = 'http://monitoring.bbta3.bppt.go.id/v1/monitor/waterfall/';
                this.URL_PDF = 'http://monitoring.bbta3.bppt.go.id/v1/monitor/pdf/';
                break;
        }
    }

    ambilAtributAngin(date_from, date_to) {
        let header = new Headers({'Content-Type': 'Application/json'});
        let qwerty = localStorage.getItem('qwerty');
        header.set('Authorization', `token ${qwerty}`);
        let options = new RequestOptions({headers: header});

        return this.http.get(`${this.URL_ANGIN}${date_from}/${date_to}/`, options)
            .map(
                (res: Response) => {
                    return res.json();
                }
            )
            .catch(
                (err: Response | any) => {
                    if (err instanceof Response) {
                        return Observable.throw(err.json());
                    }

                    else {
                        return err.message;
                    }
                }
            );
    }

    ambilWindroseAngin(date_from, date_to, vmax, step) {
        let header = new Headers({'Content-Type': 'application/json'});
        let qwerty = localStorage.getItem('qwerty');
        header.set('Authorization', `token ${qwerty}`);
        let parameter = new URLSearchParams();
        parameter.set('vmax', vmax);
        parameter.set('step', step);

        let options = new RequestOptions({headers: header, search: parameter});

        return this.http.get(`${this.URL_WINDROSE}${date_from}/${date_to}/`, options)
            .map(
                (res: Response) => {
                    return res.json();
                }
            )
            .catch(
                (err: Response | any) => {
                    if (err instanceof Response) {
                        return Observable.throw(err.json());
                    }

                    else {
                        return err.message;
                    }
                }
            );
    }

    ambilRMSAngin(vmax, step, arah) {
        let header = new Headers({'Content-Type': 'application/json'});
        let qwerty = localStorage.getItem('qwerty');
        header.set('Authorization', `token ${qwerty}`);
        let parameter = new URLSearchParams();
        parameter.set('vmax', vmax);
        parameter.set('step', step);
        parameter.set('arah', arah);

        let options = new RequestOptions({headers: header, search: parameter});

        return this.http.get(`${this.URL_RMS}`, options)
            .map(
                (res: Response) => {
                    return res.json();
                }
            )
            .catch(
                (err: Response | any) => {
                    if (err instanceof Response) {
                        return Observable.throw(err.json());
                    }

                    else {
                        return err.message;
                    }
                }
            );
    }

    ambilWaterfallAngin(date_from, date_to, vmax, step, arah, wkt_awal, wkt_akhir, simplified) {
        let header = new Headers({'Content-Type': 'application/json'});
        let qwerty = localStorage.getItem('qwerty');
        header.set('Authorization', `token ${qwerty}`);
        let parameter = new URLSearchParams();
        parameter.set('vmax', vmax);
        parameter.set('step', step);
        parameter.set('arah', arah);
        parameter.set('simplified', simplified);

        if (simplified) {
            parameter.set('wkt_awal', '00:00');
            parameter.set('wkt_akhir', '23:59');
            parameter.set('step', '0');
            parameter.set('vmax', '0');
        }
        else {
            parameter.set('wkt_awal', wkt_awal);
            parameter.set('wkt_akhir', wkt_akhir);
            parameter.set('step', step);
            parameter.set('vmax', vmax);
        }

        let options = new RequestOptions({headers: header, search: parameter});

        return this.http.get(`${this.URL_WATERFALL}${date_from}/${date_to}/`, options)
            .map(
                (res: Response) => {
                    return res.json();
                }
            )
            .catch(
                (err: Response | any) => {
                    if (err instanceof Response) {
                        return Observable.throw(err.json());
                    }

                    else {
                        return err.message;
                    }
                }
            );
    }

    ambilPdfAngin(date_from, date_to) {
        let header = new Headers({'Content-Type': 'Application/json'});
        let qwerty = localStorage.getItem('qwerty');
        header.set('Authorization', `token ${qwerty}`);
        let options = new RequestOptions({headers: header});

        return this.http.get(`${this.URL_PDF}${date_from}/${date_to}/`, options)
            .map(
                (res: Response) => {
                    return res.json();
                }
            )
            .catch(
                (err: Response | any) => {
                    if (err instanceof Response) {
                        return Observable.throw(err.json());
                    }

                    else {
                        return err.message;
                    }
                }
            );
    }
}
