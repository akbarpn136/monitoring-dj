/**
 * Created by USER on 2/20/2017.
 */
import {Route, RouterModule} from '@angular/router';
import {AnginComponent} from "./angin/angin.component";
import {WindroseComponent} from "./windrose/windrose.component";
import {RmsComponent} from "./rms/rms.component";
import {WaterfallComponent} from "./waterfall/waterfall.component";
import {PdfComponent} from "./pdf/pdf.component";
import {LoginComponent} from "./login/login.component";

const APP_ROUTES: Route[] = [
    {path: 'rms', component: RmsComponent},
    {path: 'waterfall', component: WaterfallComponent},
    {path: 'pdf', component: PdfComponent},
    {path: 'windrose', component: WindroseComponent},
    {path: 'angin', component: AnginComponent},
    {path: 'login', component: LoginComponent},
    {path: '', component: AnginComponent},
    {path: '**', redirectTo:'', pathMatch:'full'},
];

export const route = RouterModule.forRoot(APP_ROUTES);
