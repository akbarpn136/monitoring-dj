import {Injectable} from '@angular/core';
import {Http, Response, Headers, RequestOptions, URLSearchParams} from "@angular/http";

import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import {Observable} from "rxjs";

@Injectable()
export class ProsesService {
    private URL_ANGIN = 'http://localhost:8000/v1/monitor/angin/';
    private URL_WINDROSE = 'http://localhost:8000/v1/monitor/windrose/';

    constructor(private http: Http) {
    }

    ambilAtributAngin(date_from, date_to) {
        let header = new Headers({'Content-Type': 'Application/json'});
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
}
