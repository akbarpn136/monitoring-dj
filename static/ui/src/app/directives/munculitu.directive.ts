import {Directive, Output, EventEmitter, HostListener, Input, HostBinding} from '@angular/core';

@Directive({
    selector: '[anMunculitu]'
})
export class MunculituDirective {
    visible:boolean = false;

    @Input() set isVisible(val) {
        this.isShow = val
    };
    @Output() status = new EventEmitter<any>();
    @HostBinding('class.show') isShow = this.isVisible;
    @HostListener('click') onMouseClicked() {
        this.visible = !this.visible;
        this.status.emit(this.visible);
    }
}
