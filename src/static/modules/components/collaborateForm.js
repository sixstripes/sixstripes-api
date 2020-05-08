import axios from 'axios';


class CollaborateForm {
  constructor(dataType) {
    this.dataType = dataType;
    this.form = document.querySelector(".js-collaborate-form");
    this.fieldsContainer = this.form.querySelector(".js-dynamic-fields");
  }

  clearFields() {
    this.fieldsContainer.innerHTML = '';
  }

  getEndpointInfo() {
    return axios.get('/?format=openapi').then(response => {
      return response.data.definitions[this.dataType]
    });
  }

  createField(fieldId, fieldProperty) {
    console.log(fieldId)
    console.log(fieldProperty)
    const fieldLabel = document.createElement('label')
    fieldLabel.setAttribute('for', fieldId)
    fieldLabel.innerHTML= fieldProperty.title
    const fieldElement = document.createElement('input')
    fieldElement.setAttribute('id', fieldId)

    this.fieldsContainer.appendChild(fieldLabel);
    this.fieldsContainer.appendChild(fieldElement);
  }

  populateFields() {
    this.getEndpointInfo().then((schema) => {
      const properties = schema.properties;
      Object.entries(properties).map((property) => {
        const [name, fieldProperty] = property
        this.createField(name, fieldProperty);
      });
    })
  }
}

export default CollaborateForm;
