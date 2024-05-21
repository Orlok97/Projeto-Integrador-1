
M.AutoInit();

function closeMessage() {
    document.querySelector('#alert').remove()
}
function showImage() {
    let file = document.querySelector('#file')
    let preview = document.querySelector('#preview')

    if (file.files && file.files[0]) {
        let reader = new FileReader();
        reader.onload = function (e) {
            preview.style.width="310px";
            preview.style.height="150px";
            preview.style.display = 'block'
            preview.src = e.target.result;
        }
        reader.readAsDataURL(file.files[0]);
    }
    document.querySelector('#closePreview').setAttribute('class','btn-floating red accent-3 tooltipped');
    document.querySelector('#delete_icon').setAttribute('class','material-icons small red lighten-1');
    document.querySelector('#delete_icon').innerHTML = 'delete';
}

function showImageEdit(id) {
    let file = document.querySelector('#file-'+id)
    let preview = document.querySelector('#preview-'+id)

    if (file.files && file.files[0]) {
        let reader = new FileReader();
        reader.onload = function (e) {
            preview.style.display = 'block'
            preview.src = e.target.result;
        }
        reader.readAsDataURL(file.files[0]);
    }
}


function closePreview() {
    document.querySelector('#file').value = '';
    document.querySelector('#preview').src = '';
    document.querySelector('#preview').style.width='0px';
    document.querySelector('#preview').style.height='0px';
    document.querySelector('#closePreview').setAttribute('class','tootipped');
    document.querySelector('#delete_icon').innerHTML = '';
    console.log('preview fechado');
}

function deletarSolicitacao(id){
    if(confirm('deseja deletar essa solicitação?')){
        window.location.href='/delete/'+id;
    }
}
// document.querySelector('#file').addEventListener('change', showImage);
