import { Component } from '@angular/core'
import { FormGroup, FormControl } from '@angular/forms'
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap'
import { first } from 'rxjs'
import {
  DocumentSource,
  PaperlessConsumptionTemplate,
} from 'src/app/data/paperless-consumption-template'
import { PaperlessCorrespondent } from 'src/app/data/paperless-correspondent'
import { PaperlessDocumentType } from 'src/app/data/paperless-document-type'
import { PaperlessStoragePath } from 'src/app/data/paperless-storage-path'
import { ConsumptionTemplateService } from 'src/app/services/rest/consumption-template.service'
import { CorrespondentService } from 'src/app/services/rest/correspondent.service'
import { DocumentTypeService } from 'src/app/services/rest/document-type.service'
import { StoragePathService } from 'src/app/services/rest/storage-path.service'
import { UserService } from 'src/app/services/rest/user.service'
import { SettingsService } from 'src/app/services/settings.service'
import { EditDialogComponent } from '../edit-dialog.component'

const SOURCE_OPTIONS = [
  {
    id: DocumentSource.ConsumeFolder,
    name: $localize`Documents uploaded via consume folder`,
  },
  {
    id: DocumentSource.ApiUpload,
    name: $localize`Documents uploaded via api upload`,
  },
  {
    id: DocumentSource.MailFetch,
    name: $localize`Documents uploaded via mail fetch`,
  },
]

@Component({
  selector: 'pngx-consumption-template-edit-dialog',
  templateUrl: './consumption-template-edit-dialog.component.html',
  styleUrls: ['./consumption-template-edit-dialog.component.scss'],
})
export class ConsumptionTemplateEditDialogComponent extends EditDialogComponent<PaperlessConsumptionTemplate> {
  templates: PaperlessConsumptionTemplate[]
  correspondents: PaperlessCorrespondent[]
  documentTypes: PaperlessDocumentType[]
  storagePaths: PaperlessStoragePath[]

  constructor(
    service: ConsumptionTemplateService,
    activeModal: NgbActiveModal,
    correspondentService: CorrespondentService,
    documentTypeService: DocumentTypeService,
    storagePathService: StoragePathService,
    userService: UserService,
    settingsService: SettingsService
  ) {
    super(service, activeModal, userService, settingsService)

    correspondentService
      .listAll()
      .pipe(first())
      .subscribe((result) => (this.correspondents = result.results))

    documentTypeService
      .listAll()
      .pipe(first())
      .subscribe((result) => (this.documentTypes = result.results))

    storagePathService
      .listAll()
      .pipe(first())
      .subscribe((result) => (this.storagePaths = result.results))
  }

  getCreateTitle() {
    return $localize`Create new consumption template`
  }

  getEditTitle() {
    return $localize`Edit consumption template`
  }

  getForm(): FormGroup {
    return new FormGroup({
      name: new FormControl(null),
      account: new FormControl(null),
      filter_filename: new FormControl(null),
      filter_path: new FormControl(null),
      order: new FormControl(null),
      sources: new FormControl([]),
      assign_tags: new FormControl([]),
      assign_owner: new FormControl(null),
      assign_document_type: new FormControl(null),
      assign_correspondent: new FormControl(null),
      assign_storage_path: new FormControl(null),
      assign_view_users: new FormControl(null),
      assign_view_groups: new FormControl(null),
      assign_change_users: new FormControl(null),
      assign_change_groups: new FormControl(null),
    })
  }

  get sourceOptions() {
    return SOURCE_OPTIONS
  }
}