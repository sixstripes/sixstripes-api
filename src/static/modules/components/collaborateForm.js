import { createField } from '../utils/fields';

const endpoints = {
  "athlet": [
    {name: "name", title: "Name", type: "text"},
    {name: "country", title: "Country", type: "enum", optionsUrl: "/v1/countries/"},
    {name: "reference", title: "Reference", type: "uri"},
    {name: "start_birth_date", title: "Birth Date", type: "date"},
    {name: "start_death_date", title: "Death Date", type: "date"},
    {name: "sexual_orientation", title: "Sexual Orientation", type: "enum", optionsUrl: "/v1/sexual-orientations/"},
    {name: "sport", title: "Sport", type: "enum", optionsUrl: "/v1/sports/"}
  ],
  "digital-influencer": [
    {name: "name", title: "Name", type: "text"},
    {name: "country", title: "Country", type: "enum", optionsUrl: "/v1/countries/"},
    {name: "reference", title: "Reference", type: "uri"},
    {name: "start_birth_date", title: "Birth Date", type: "date"},
    {name: "start_death_date", title: "Death Date", type: "date"},
    {name: "sexual_orientation", title: "Sexual Orientation", type: "enum", optionsUrl: "/v1/sexual-orientations/"},
    {name: "subscribers", title: "Subscribers", type: "integer"},
    {name: "views", title: "Views", type: "integer"},
    {name: "url", title: "URL", type: "uri"},
    {name: "social_media_username", title: "Username", type: "text"},
    {name: "main_social_medias", title: "Social Medias", type: "multiple-enum", optionsUrl: "/v1/social-medias/"},
  ],
  "movie": [
    {name: "name", title: "Name", type: "text"},
    {name: "year", title: "Year", type: "integer"},
    {name: "countries", title: "Countries", type: "multiple-enum", optionsUrl: "/v1/countries/"},
    {name: "reference", title: "Reference", type: "uri"},
    {name: "gender", title: "Genders", type: "multiple-enum", optionsUrl: "/v1/movie-genders/"},
    {name: "directors", title: "Directors", type: "multiple"},
    {name: "cast", title: "Cast", type: "multiple"}
  ],
  "musician": [
    {name: "name", title: "Name", type: "text"},
    {name: "country", title: "Country", type: "enum", optionsUrl: "/v1/countries/"},
    {name: "reference", title: "Reference", type: "uri"},
    {name: "start_birth_date", title: "Birth Date", type: "date"},
    {name: "start_death_date", title: "Death Date", type: "date"},
    {name: "sexual_orientation", title: "Sexual Orientation", type: "enum", optionsUrl: "/v1/sexual-orientations/"},
    {name: "musical_genders", title: "Musical Genders", type: "multiple-enum", optionsUrl: "/v1/musical-genders/"}
  ],
  "politician": [
    {name: "name", title: "Name", type: "text"},
    {name: "country", title: "Country", type: "enum", optionsUrl: "/v1/countries/"},
    {name: "reference", title: "Reference", type: "uri"},
    {name: "start_birth_date", title: "Birth Date", type: "date"},
    {name: "start_death_date", title: "Death Date", type: "date"},
    {name: "sexual_orientation", title: "Sexual Orientation", type: "enum", optionsUrl: "/v1/sexual-orientations/"},
    {name: "occupations", title: "Occupations", type: "multiple-enum", optionsUrl: "/v1/occupations/"}
  ],
  "scientist": [
    {name: "name", title: "Name", type: "text"},
    {name: "country", title: "Country", type: "enum", optionsUrl: "/v1/countries/"},
    {name: "reference", title: "Reference", type: "uri"},
    {name: "start_birth_date", title: "Birth Date", type: "date"},
    {name: "start_death_date", title: "Death Date", type: "date"},
    {name: "sexual_orientation", title: "Sexual Orientation", type: "enum", optionsUrl: "/v1/sexual-orientations/"},
    {name: "occupations", title: "Occupations", type: "multiple-enum", optionsUrl: "/v1/occupations/"}
  ],
}

const excludeFields = ["end_death_date", "end_birth_date"]

class CollaborateForm {
  constructor(dataType) {
    this.dataType = dataType;
    this.form = document.querySelector(".js-collaborate-form");
    this.fieldsContainer = this.form.querySelector(".js-dynamic-fields");
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
