<template>
  <div>
      <nav class="navbar">
        <div class="logo">
            APSİYON KOMBİ
        </div>
        <div class="context">
            <a href="#">Ürünlerimiz</a>
            <a href="#">Bayi-Servis</a>
            <a href="#">Hakkımızda</a>
            <a href="#">İletişim</a>
        </div>
      </nav>
  </div>
</template>

<script>
export default {
  name: 'Header',

}
</script>


<style scoped>

.navbar {
    background-color: white;
    border-bottom: 1px solid gray;
    width: 90%;
    margin:40px auto 0px;
}
.logo {
    font-size: 2em;
    font-weight: bold;
    color: #A57548; 
    border-bottom: 1px solid black;
    margin: 0px auto;
    width: 500px;
}

.context {
    font-size: 1.2em;
    width: 500px;
    margin: 10px auto;
}

.context a {
    text-decoration: none;
    margin-right: 10px;
    color: #A57548;
    font-weight: bold;
}

.context a:hover {
    color: #FCD7AD;
}


@media only screen and (max-width: 820px) {
  .navbar {
    width: 100%;
  }
}

</style>