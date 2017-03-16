import {Directive, HostBinding, HostListener} from '@angular/core';

@Directive({
    selector: '[anMunculini]'
})
export class MunculiniDirective {

    constructor() {
    }

    @HostBinding('class.show') clk = false;

    @HostListener('click') onMouseClicked() {
        this.clk = true;
    }

    @HostListener('mouseleave') onMouseLeaved() {
        this.clk = false;
    }

}
