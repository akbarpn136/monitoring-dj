import {Component, OnInit} from '@angular/core';
import {FormGroup, FormBuilder, Validators} from "@angular/forms";

@Component({
    selector: 'ui-windrose',
    templateUrl: './windrose.component.html',
    styleUrls: ['./windrose.component.css']
})
export class WindroseComponent implements OnInit {
    windroseForm: FormGroup;
    title: string;
    deskripsi: string;
    private isShow: boolean = false;

    constructor(private fb: FormBuilder) {
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
        this.isShow = true;
        console.log(obj);
    }
}
