  document.addEventListener('DOMContentLoaded', function() {
      // Next button click event
      var questionTypeSection = $('#step1');
      var questionData = $('#step2')
      var tfCorrectAnswer = $('#tfCorrectAnswer');
      var mcOptions = $('#additionalOptionMultipleChoice');
      document.querySelectorAll('.next_step').forEach(function(nextButton) {
          nextButton.addEventListener('click', function(e) {
              e.preventDefault();
              var selectedType = $('input[name="question_type"]:checked').val();
              questionTypeSection.addClass("d-none");
              questionData.removeClass("d-none");
              if (selectedType == 'tf') {
                  tfCorrectAnswer.removeClass("d-none");
                  mcOptions.addClass("d-none");
              } else if (selectedType == 'mc') {
                  tfCorrectAnswer.addClass("d-none");
                  mcOptions.removeClass("d-none");
              }
          });
      });
      // Previous button click event
      document.querySelectorAll('.prev_step').forEach(function(prevButton) {
          prevButton.addEventListener('click', function(e) {
              e.preventDefault();
              questionTypeSection.removeClass("d-none");
              tfCorrectAnswer.addClass("d-none");
              mcOptions.addClass("d-none");
              questionData.addClass("d-none");
          });
      });
  });


$(document).ready(function() {
    $('#add_more').click(function() {
        var totalFormsInput = $('#id_form-TOTAL_FORMS');
        totalFormsInput.val(parseInt(totalFormsInput.val()) + 1);
        var formGroupClone = $('#form_group_template').clone().removeAttr('id').show();
        var formGroupsContainer = $('#form_groups_container');
        var newIndex = formGroupsContainer.children().length ;
        formGroupClone.find('[name]').each(function() {
            var oldName = $(this).attr('name');
            $(this).attr('name', oldName.replace('0', newIndex ));
        });
        formGroupsContainer.append(formGroupClone);
    });

    $(document).on('click', '.delete_option', function() {
        $(this).closest('.form-group').remove();
    });
});
