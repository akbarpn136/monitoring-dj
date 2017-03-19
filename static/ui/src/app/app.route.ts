/**
 * Created by USER on 2/20/2017.
 */
import {Route, RouterModule} from '@angular/router';
import {AnginComponent} from "./angin/angin.component";
import {WindroseComponent} from "./windrose/windrose.component";
import {RmsComponent} from "./rms/rms.component";
import {WaterfallComponent} from "./waterfall/waterfall.component";

const APP_ROUTES: Route[] = [
    {path: 'rms', component: RmsComponent},
    {path: 'waterfall', component: WaterfallComponent},
    {path: 'pdf', component: AnginComponent},
    {path: 'windrose', component: WindroseComponent},
    {path: 'angin', component: AnginComponent},
    {path: '', component: AnginComponent},
    {path: '**', redirectTo:'', pathMatch:'full'},
];

export const route = RouterModule.forRoot(APP_ROUTES);
