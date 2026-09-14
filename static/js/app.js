
document.addEventListener('DOMContentLoaded', ()=>{
  const input = document.getElementById('q');
  if(input){
    input.addEventListener('keypress', (e)=>{
      if(e.key==='Enter'){
        const url = new URL(window.location);
        url.searchParams.set('q', e.target.value);
        window.location = url.toString();
      }
    });
  }
});
function filtrarCategoria(cat){
  const url = new URL(window.location);
  if(cat) url.searchParams.set('categoria', cat);
  else url.searchParams.delete('categoria');
  window.location = url.toString();
}
function filtrarRegion(reg){
  const url = new URL(window.location);
  if(reg) url.searchParams.set('region', reg);
  else url.searchParams.delete('region');
  window.location = url.toString();
}
