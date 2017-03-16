import {Component} from '@angular/core';
import {ProsesService} from "./services/proses.service";

@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.css'],
    providers: [ProsesService]
})
export class AppComponent {
    title = 'app works!';
}
