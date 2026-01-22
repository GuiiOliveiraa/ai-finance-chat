const chat = document.getElementById("chat");
const input = document.getElementById("input");

input.addEventListener("keydown", e=>{
  if(e.key==="Enter") send();
})

function addMsg(text, type){
  const div = document.createElement("div");
  div.classList.add("msg", type);
  div.innerText = text;
  chat.appendChild(div);
  chat.scrollTop = chat.scrollHeight;
}

async function send(){
  const msg = input.value.trim();
  if(!msg) return;

  addMsg(msg,"user");
  input.value="";

  addMsg("Digitando...","bot");

  const res = await fetch("http://localhost:8000/chat",{
    method:"POST",
    headers:{"Content-Type":"application/json"},
    body:JSON.stringify({message:msg})
  });

  const data = await res.json();

  chat.lastChild.remove(); // remove "Digitando..."
  addMsg(data.response,"bot");
}
