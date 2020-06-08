import { createField } from '../utils/fields';
import axios from 'axios';

const endpoints = {
  "athlet": [
    {name: "name", title: "Name", type: "text", required: true},
    {name: "country", title: "Country", type: "enum", optionsUrl: "/v1/countries/", required: false},
    {name: "reference", title: "Reference", type: "uri", required: true},
    {name: "start_birth_date", title: "Birth Date", type: "date", required: false},
    {name: "start_death_date", title: "Death Date", type: "date", required: false},
    {name: "sexual_orientation", title: "Sexual Orientation", type: "enum", optionsUrl: "/v1/sexual-orientations/", required: false},
    {name: "sport", title: "Sport", type: "enum", optionsUrl: "/v1/sports/", required: true}
  ],
  "digital-influencer": [
    {name: "name", title: "Name", type: "text", required: true},
    {name: "country", title: "Country", type: "enum", optionsUrl: "/v1/countries/", required: false},
    {name: "reference", title: "Reference", type: "uri", required: true},
    {name: "start_birth_date", title: "Birth Date", type: "date", required: false},
    {name: "start_death_date", title: "Death Date", type: "date", required: false},
    {name: "sexual_orientation", title: "Sexual Orientation", type: "enum", optionsUrl: "/v1/sexual-orientations/", required: false},
    {name: "subscribers", title: "Subscribers", type: "integer", required: false},
    {name: "views", title: "Views", type: "integer", required: false},
    {name: "url", title: "URL", type: "uri", required: false},
    {name: "social_media_username", title: "Username", type: "text", required: false},
    {name: "main_social_medias", title: "Social Medias", type: "multiple-enum", optionsUrl: "/v1/social-medias/", required: false},
  ],
  "movie": [
    {name: "name", title: "Name", type: "text", required: true},
    {name: "year", title: "Year", type: "integer", required: false},
    {name: "countries", title: "Countries", type: "multiple-enum", optionsUrl: "/v1/countries/", required: false},
    {name: "reference", title: "Reference", type: "uri", required: true},
    {name: "genders", title: "Genders", type: "multiple-enum", optionsUrl: "/v1/movie-genders/", required: false},
    {name: "directors", title: "Directors", type: "multiple", required: false},
    {name: "cast", title: "Cast", type: "multiple", required: false}
  ],
  "musician": [
    {name: "name", title: "Name", type: "text", required: true},
    {name: "country", title: "Country", type: "enum", optionsUrl: "/v1/countries/", required: false},
    {name: "reference", title: "Reference", type: "uri", required: true},
    {name: "start_birth_date", title: "Birth Date", type: "date", required: false},
    {name: "start_death_date", title: "Death Date", type: "date", required: false},
    {name: "sexual_orientation", title: "Sexual Orientation", type: "enum", optionsUrl: "/v1/sexual-orientations/", required: false},
    {name: "musical_genders", title: "Musical Genders", type: "multiple-enum", optionsUrl: "/v1/musical-genders/", required: false}
  ],
  "politician": [
    {name: "name", title: "Name", type: "text", required: true},
    {name: "country", title: "Country", type: "enum", optionsUrl: "/v1/countries/", required: false},
    {name: "reference", title: "Reference", type: "uri", required: true},
    {name: "start_birth_date", title: "Birth Date", type: "date", required: false},
    {name: "start_death_date", title: "Death Date", type: "date", required: false},
    {name: "sexual_orientation", title: "Sexual Orientation", type: "enum", optionsUrl: "/v1/sexual-orientations/", required: false},
    {name: "occupations", title: "Occupations", type: "multiple-enum", optionsUrl: "/v1/occupations/", required: true}
  ],
  "scientist": [
    {name: "name", title: "Name", type: "text", required: true},
    {name: "country", title: "Country", type: "enum", optionsUrl: "/v1/countries/", required: false},
    {name: "reference", title: "Reference", type: "uri", required: true},
    {name: "start_birth_date", title: "Birth Date", type: "date", required: false},
    {name: "start_death_date", title: "Death Date", type: "date", required: false},
    {name: "sexual_orientation", title: "Sexual Orientation", type: "enum", optionsUrl: "/v1/sexual-orientations/", required: false},
    {name: "occupations", title: "Occupations", type: "multiple-enum", optionsUrl: "/v1/occupations/", required: false}
  ],
}

const excludeFields = ["end_death_date", "end_birth_date"]

class CollaborateForm {
  constructor(dataType) {
    this.dataType = dataType;
    this.form = document.querySelector(".js-collaborate-form");
    this.form.onsubmit = this.beforeSend;
    this.fieldsContainer = this.form.querySelector(".js-dynamic-fields");
  }

  beforeSend(event) {
    const formData = new FormData(event.target);
    const finalData = {};
    for (let field of formData.entries()) {
      let [name, value] = field;
      const fieldElement = this.querySelector(`[name="${name}"`);
      if (fieldElement.dataset.fieldType === "multiple" || fieldElement.dataset.fieldType === "multiple-enum") {
        const fieldDataString = fieldElement.value;
        if (fieldDataString) {
          const fieldData = JSON.parse(fieldDataString);
          value = fieldData.map(data => {
            return data.value;
          });
        } else {
          value = [];
        }
      }
      finalData[name] = value;
    }
    axios.post('/suggestions/', {data: finalData}).then(response => {
      alert('Enviado com sucesso!');
      document.querySelector(".js-collaborate-form > .js-dynamic-fields").innerHTML = '';
    });
    return false;
  }

  clearFields() {
    this.fieldsContainer.innerHTML = '';
  }

  appendFieldToForm(field) {
    Promise.resolve(createField(field)).then(element => {
      this.fieldsContainer.appendChild(element);
    });
  }

  populateFields() {
    endpoints[this.dataType].map(field => {
      this.appendFieldToForm(field);
    });
  }
}

export default CollaborateForm;
