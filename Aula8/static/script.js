
function deleteTerm(designation){
    $.ajax("/terms/" + designation, {
        type: "DELETE"

    })
}