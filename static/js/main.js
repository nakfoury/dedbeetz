$(document).ready((function () {
  $('form#fileUpload > button').click(function (event) {
    event.preventDefault();
    $(this).prop("disabled", true);
    const formData = new FormData($('form#fileUpload')[0]);
    $.post("api/upload", formData, function (response) {
      console.log(response)
    });
  });
}));


//     $('form#fileUpload').submit(function (event) {
//       event.preventDefault();
//       const form_data = new FormData($(this)[0]);  //$(this).serialize();  // encode form elements for submission
//       console.log(form_data);
//       $.post("api/upload", form_data, function (response) {
//         console.log(response)
//       });
//     })
//   })
// }));
