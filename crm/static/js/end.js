
const formset_factory = document.querySelector('#formset_factory');

if (formset_factory){
    document.querySelectorAll("[id$='-DELETE']").forEach(e=>{
        e.remove();
    });
    document.querySelectorAll("[for$='-DELETE']").forEach(e=>{
        e.remove();
    });
}