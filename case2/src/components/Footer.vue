<template>
    <div>
        <footer class="footer">
            <div class="allFooter">
                 <div class="social-media">
                <div class="social">
                <i class="fab fa-facebook"></i>
                <i class="fab fa-instagram-square"></i>
                <i class="fab fa-twitter-square"></i>
                </div>
                <div class="me">
                    Made by OmerSari for Apsiyon
                    <a href="https://www.github.com/omeersari" target="_blank">GitHub  <i class="fab fa-github-square"></i></a>
                </div>
            </div>
            <div class="context">
            <h4> <a href="#">Apsiyon Kombi</a> </h4>
            <a href="#">Ürünlerimiz</a>
            <a href="#">Bayi-Servis</a>
            <a href="#">Hakkımızda</a>
            <a href="#">İletişim</a>
            </div>
            
            </div>
           
        </footer>
    </div>
</template>

<script>
export default {
    name:"Footer",
}
</script>

<style scoped>

.footer {
    background-color: lightgray;
    color: black;
}

.allFooter {
    width: 90%;
    margin: 0 auto;
}
.social-media {
    padding-top:25px;
    font-size: 1.5em;
    display: flex;
    justify-content: space-between;
}

.social i {
    margin-right: 10px;
}

.me {
    display: flex;
    flex-direction: column;
}
.me a {
    text-decoration: none;
    color: black;
}

.context {
    display: flex;
    text-align: left;
    flex-direction: column;
    margin-top: 15px;
}

.context a {
    margin-top: 5px;
    text-decoration: none;
    color: black;
}

</style>