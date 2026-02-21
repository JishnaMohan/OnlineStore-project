let result=1
function add(){
    result=result+1;
    document.getElementById('output').value=result;
}

function sub(){
    if (result>1){
        result=result-1;
        document.getElementById('output').value=result;
    }
}