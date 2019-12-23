$(function(){

  $("[type=file]").on("change", function(){
    var file = this.files[0];
    var formdata = new FormData();
    formdata.append("file", file);

    $('.admin-csv-import label').text(file.name);
    $('.admin-csv-import .submit').addClass("-show");
  });
});
