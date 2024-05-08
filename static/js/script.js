
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
            preview.style.display = 'block'
            preview.src = e.target.result;
        }
        reader.readAsDataURL(file.files[0]);
    }
    document.querySelector('#closePreview').innerHTML = 'delete'
}

function showImageEdit() {
    let file = document.querySelector('#file2')
    let preview = document.querySelector('#preview2')

    if (file.files && file.files[0]) {
        let reader = new FileReader();
        reader.onload = function (e) {
            preview.style.display = 'block'
            preview.src = e.target.result;
        }
        reader.readAsDataURL(file.files[0]);
    }
    console.log(preview.src)
    document.querySelector('#closePreview').innerHTML = 'delete'
}

function showImageCreate() {
    let file = document.querySelector('#file3')
    let preview = document.querySelector('#preview3')

    if (file.files && file.files[0]) {
        let reader = new FileReader();
        reader.onload = function (e) {
            preview.style.display = 'block'
            preview.src = e.target.result;
        }
        reader.readAsDataURL(file.files[0]);
    }
    console.log(preview.src)
    document.querySelector('#closePreview').innerHTML = 'delete'
}
function closePreview() {
    document.querySelector('#file').value = ''
    document.querySelector('#preview').src = ""
    document.querySelector('#closePreview').innerHTML = ''
    console.log('preview fechado')
}

function deletarSolicitacao(id){
    if(confirm('deseja deletar essa solicitação?')){
        window.location.href='/delete/'+id;
    }
}
document.querySelector('#file').addEventListener('change', showImage);
 document.querySelector('#file2').addEventListener('change', showImageEdit);
 document.querySelector('#file3').addEventListener('change', showImageCreate);
