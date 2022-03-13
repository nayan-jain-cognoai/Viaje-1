let chunkUploads = true
let chunkSize = 50000
let labelButtonDownloadItem = true
let allowDownloadByUrl = true
let files_flight = []
var uploaded = {};
var uploadIdFilenames = {}; 
var uploaded_error = {};

var type_of_attachment = ""


let server = {
            url: 'http://127.0.0.1:8000/fp',
            process: '/process/',
            patch: '/patch/',
            revert: null,
            fetch: null,
            load: null
        }

    function onprocessfile(file,type_of_attachment){
        const csrftoken = Cookies.get('csrftoken');

        let url_parameters = get_url_vars();
        let file_id = file.id
        let filename = file.filename.replaceAll(" ","_").replaceAll("/","_").replaceAll("$","_")
        console.log(type_of_attachment)
        console.log(file.serverId)
        let options = {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json;charset=utf-8',
                  'X-CSRFToken': csrftoken
              },
              body: JSON.stringify({
                  "type_of_attachment":type_of_attachment,
                  "id_of_attachment":file.serverId,
                  "trip_pk":url_parameters["pk"],
                  "file_id":file.id,
                  "filename":filename
              })
          }

        let fetchRes = fetch("/save-attachment/", options);
        let response;

        fetchRes.then(res =>
          res.json()).then(response => {
              response = response;
              console.log(response)
          })
    }

    function ondeletefile(file,type_of_attachment){
        let url_parameters = get_url_vars();
          let trip_pk = url_parameters["pk"]
          let file_id = file.filename.replaceAll(" ","_")

          fetch('/delete-attachment/?name_of_attachment='+file_id+"&trip_pk="+trip_pk+"&type_of_attachment="+type_of_attachment)
              .then(response => response.json())
              .then(data => console.log(data));


          if(file.id in uploaded) delete uploaded[file.id];
    }

    function onerror(file,status,error){
        console.log('File error: [' + error + ']   file: [' + file.id + '], status [' + status + ']');
        if(file.id in uploaded) {
            delete uploaded[file.id];
        }
        uploaded_error[file.id] = true;         
    }
      
    function set_type_of_attachment(attachment){
        type_of_attachment = attachment
    }


    $('#file_pond_input').filepond();
    $('#file_pond_input').filepond('allowMultiple', true);
    $('#file_pond_input').filepond.setOptions({
    chunkUploads: chunkUploads,
    chunkSize: chunkSize,
    labelButtonDownloadItem: labelButtonDownloadItem, // by default 'Download file'
    allowDownloadByUrl: allowDownloadByUrl, // by default downloading by URL disabled,
    files: files_flight,
    server: server,
    onaddfile: function(error, file) {},
    onprocessfile: function(error, file) {
      onprocessfile(file,type_of_attachment)
    },
    onremovefile: function(error, file) {
        ondeletefile(file,type_of_attachment)
    },
    onerror: function(error, file, status) {
      onerror(file,status)
    }

    });