import axios from 'axios';
import datepicker from 'js-datepicker';
import Tagify from '@yaireo/tagify';

function createTextField(field) {
  const fieldLabel = document.createElement('label');
  fieldLabel.setAttribute('for', field.name);
  fieldLabel.innerHTML= field.title;
  const fieldElement = document.createElement('input');
  fieldElement.setAttribute('id', field.name);
  fieldElement.setAttribute('name', field.name);
  fieldElement.setAttribute('data-field-type', field.type);

  const div = document.createElement('div');
  div.setAttribute("class", field.name);
  div.appendChild(fieldLabel);
  div.appendChild(fieldElement);

  return div;
};

function createDateField(field) {
  const textField = createTextField(field);
  const input = textField.querySelector("input");
  datepicker(input, {});
  return textField;
}

function createMultipleField(field) {
  const textField = createTextField(field);
  const input = textField.querySelector("input");
  new Tagify(input);
  return textField;
}

function getEnumData(url, data = []) {
  return axios.get(url).then(response => {
    const responseData = response.data
    data.push(...responseData.results)
    if (responseData.next) return getEnumData(responseData.next, data);
    return data;
  });
}

function createMultipleEnumField(field){
  return getEnumData(field.optionsUrl).then(data => {
    const textField = createTextField(field);
    const input = textField.querySelector("input");
    new Tagify(input, {
      enforceWhitelist: true,
      whitelist: data.map((item) => {
        return item.name;
      })
    });
    return textField;
  })
}

function createEnumField(field) {
  return getEnumData(field.optionsUrl).then(data => {
    const fieldLabel = document.createElement('label');
    fieldLabel.setAttribute('for', field.name);
    fieldLabel.innerHTML= field.title;
    const fieldElement = document.createElement('select');
    fieldElement.setAttribute('id', field.name);
    fieldElement.setAttribute('name', field.name);
    fieldElement.setAttribute('data-field-type', field.type);

    data.map(item => {
      const optionElement = document.createElement('option');
      optionElement.setAttribute('value', item.name);
      optionElement.innerHTML = item.name;
      fieldElement.appendChild(optionElement);
    })

    const div = document.createElement('div');
    div.setAttribute("class", field.name);
    div.appendChild(fieldLabel);
    div.appendChild(fieldElement);

    return div;
  })
}

function createIntegerField(field) {
  const textField = createTextField(field);
  const input = textField.querySelector("input");
  input.setAttribute('type', 'number');
  input.setAttribute('min', 0);
  return textField;
}

function createURIField(field) {
  const textField = createTextField(field);
  const input = textField.querySelector("input");
  input.setAttribute('type', 'url');
  return textField;
}

const fieldRelation = {
  'text': createTextField,
  'enum': createEnumField,
  'integer': createIntegerField,
  'date': createDateField,
  'uri': createURIField,
  'multiple': createMultipleField,
  'multiple-enum': createMultipleEnumField,
}

function createField(field) {
  const fieldFunction = fieldRelation[field.type];
  return fieldFunction(field);
}

export {
  createField
};
