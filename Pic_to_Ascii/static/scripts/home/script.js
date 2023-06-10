function copyText() {
  var textarea = document.getElementById("response");
  textarea.select();
  document.execCommand("copy")
  alert("Copied Successfully!")
}

const dropZone = document.getElementById("drop-zone");
const outputContainer = document.getElementById("response");
const fileInput = document.getElementById("file-input")

dropZone.addEventListener('dragover', (e) => {
  e.preventDefault();
  dropZone.classList.add('highlight');
});

dropZone.addEventListener('dragleave', () => {
  dropZone.classList.remove('highlight');
});

dropZone.addEventListener('drop', (e) => {
  e.preventDefault();
  dropZone.classList.remove('highlight');

  const file = e.dataTransfer.files[0];

  // Check if the dropped file is in PNG or JPG format
  if (file && (file.type === 'image/png' || file.type === 'image/jpeg')) {
    uploadFile(file);
  } else {
    alert('Invalid file format');
  }

});

dropZone.addEventListener('click',() => {
  fileInput.click()
});

fileInput.addEventListener('change', (e) => {
  const file = e.target.files[0];
  if (file && (file.type === 'image/png' || file.type === 'image/jpeg')) {
    uploadFile(file);
  } else {
    alert("Invalid file format");
  }
})

function uploadFile(file) {
  const formData = new FormData();
    formData.append('file', file);

    // Send the file to the Flask backend using an AJAX request
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/home', true);
    xhr.onload = function () {
      if (xhr.status === 200) {
        // File upload success
        const response = JSON.parse(xhr.responseText);
        outputContainer.textContent = response.output;
        alert('File uploaded successfully');
      } else {
        // File upload failed
        alert('Error uploading file');
      }
    };
    xhr.send(formData);
}

