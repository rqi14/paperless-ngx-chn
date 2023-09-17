import { HttpClientTestingModule } from '@angular/common/http/testing'
import { ComponentFixture, TestBed } from '@angular/core/testing'
import { FormsModule, ReactiveFormsModule } from '@angular/forms'
import { NgbActiveModal, NgbModule } from '@ng-bootstrap/ng-bootstrap'
import { NgSelectModule } from '@ng-select/ng-select'
import { IfOwnerDirective } from 'src/app/directives/if-owner.directive'
import { IfPermissionsDirective } from 'src/app/directives/if-permissions.directive'
import { SafeHtmlPipe } from 'src/app/pipes/safehtml.pipe'
import { NumberComponent } from '../../input/number/number.component'
import { PermissionsGroupComponent } from '../../input/permissions/permissions-group/permissions-group.component'
import { PermissionsUserComponent } from '../../input/permissions/permissions-user/permissions-user.component'
import { SelectComponent } from '../../input/select/select.component'
import { TagsComponent } from '../../input/tags/tags.component'
import { TextComponent } from '../../input/text/text.component'
import { ConsumptionTemplateEditDialogComponent } from './consumption-template-edit-dialog.component'
import { EditDialogMode } from '../edit-dialog.component'

describe('ConsumptionTemplateEditDialogComponent', () => {
  let component: ConsumptionTemplateEditDialogComponent
  let fixture: ComponentFixture<ConsumptionTemplateEditDialogComponent>

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [
        ConsumptionTemplateEditDialogComponent,
        IfPermissionsDirective,
        IfOwnerDirective,
        SelectComponent,
        TextComponent,
        NumberComponent,
        TagsComponent,
        PermissionsUserComponent,
        PermissionsGroupComponent,
        SafeHtmlPipe,
      ],
      providers: [NgbActiveModal],
      imports: [
        HttpClientTestingModule,
        FormsModule,
        ReactiveFormsModule,
        NgSelectModule,
        NgbModule,
      ],
    }).compileComponents()

    fixture = TestBed.createComponent(ConsumptionTemplateEditDialogComponent)
    component = fixture.componentInstance

    fixture.detectChanges()
  })

  it('should support create and edit modes', () => {
    component.dialogMode = EditDialogMode.CREATE
    const createTitleSpy = jest.spyOn(component, 'getCreateTitle')
    const editTitleSpy = jest.spyOn(component, 'getEditTitle')
    fixture.detectChanges()
    expect(createTitleSpy).toHaveBeenCalled()
    expect(editTitleSpy).not.toHaveBeenCalled()
    component.dialogMode = EditDialogMode.EDIT
    fixture.detectChanges()
    expect(editTitleSpy).toHaveBeenCalled()
  })
})