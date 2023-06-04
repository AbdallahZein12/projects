function copyText() {
    var textarea = document.getElementById("response");
    textarea.select();
    document.execCommand("copy");
    alert("Copied Successfully!")
  }