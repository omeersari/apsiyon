<template>
    <div class="contact">
       <h1>BİZE ULAŞIN</h1>
       <form class="contactForm" action="">
           <div class="first">
               <input type="text" placeholder="İsim">
               <input type="text" placeholder="E-posta">
           </div>
           <input type="text" placeholder="Konu">
           <textarea type="text" placeholder="Mesajınızı Buraya Yazınız"> </textarea>
           <button class="button">GÖNDER</button>
       </form>
       
    </div>
</template>

<script>
export default {
    name:"Main",
}
</script>

<style scoped>
.contact {
    border: 1px solid black;
    padding: 20px;
    margin-bottom: 20px;
}

.contactForm {
    width: 50%;
    margin: 10px auto;
    
}

.first {
    display: flex;
    justify-content: space-around;
    margin-bottom: 15px;
}

.contactForm input {
    display: block;
    padding:10px;
    width: 100%;
    border: none;
    border-bottom: 1px solid gray;
}

.first input {
    width: 50%;
    border: none;
    border-bottom: 1px solid gray;
    margin-right: 15px;
}

.contactForm textarea {
    margin-top: 15px;
    border: none;
    border-bottom: 1px solid gray;
    width: 100%;
    padding:10px;
}

.button {
    padding:15px;
    width: 100%;
    margin-top: 15px;
    background: lightblue;
    border: none;
    color: black;
    font-weight: bold;
    transition: 400ms all;
}

.button:hover {
    background-color: black;
    color: white;
    cursor: pointer;
}
</style>