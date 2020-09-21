<template>
    <div class="main">
       <div class="banner">
           <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto tempora iure, com
               modi vel impedit nobis iusto eos fugiat suscipit similique maiores acc
               usantium, expedita adipisci fugit eaque pra
               esentium asperiores deserunt corporis?</p>       
       </div>
        <div class="context">

            <div class="haberler">
                <div class="header">
                    <h3>Haberler</h3>
                    <h3 class="tum">tüm haberler ></h3>
                </div>
                <ul>
                    <li class="singleHaber" v-for="(item, id) in haberler" :key="id">
                        <p class="title">{{item.title | truncate(180)}}</p>
                        <p class="content"> {{item.content | truncate(80)}}</p>
                        <p class="content">{{item.date}}</p>
                    </li>
                
                </ul>
            </div>
        </div>
        <Contact />
    </div>
</template>

<script>
import Contact from "./Contact";
export default {
    name:"Main",
    components: {
        Contact
    },
    data() {
        return {
            haberler: [
                {
                    title:"Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quam culpa cupiditate dolor perferendis laudantium exercitationem!",
                    content:"Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ipsam ipsum corrupti nesciunt quis, natus saepe repellendus enim optio animi? Harum assumenda eum fuga ducimus, minus itaque atque quisquam unde voluptatem rerum odio nihil autem deserunt in at facere ea. Doloremque sapiente qui dolorum soluta provident consectetur mollitia consequatur magni at expedita explicabo est, eos ipsa odio debitis eius! Quo exercitationem ut autem beatae aliquam qui repudiandae dolor, maxime architecto sit iste perferendis, est, sed aspernatur repellat? Dolore, natus. Quis magnam voluptate sit consequuntur eum labore repellendus, in quia illum dignissimos eligendi culpa natus quas voluptates voluptatibus iure corporis non libero maiores! Dolores impedit dolorum consequuntur, molestias alias tempore? Quae recusandae itaque aspernatur sunt repellendus eaque, nesciunt laboriosam debitis a omnis explicabo commodi tempore consequatur corrupti! Minima ratione maiores necessitatibus fugiat, numquam alias recusandae dolores error consectetur et animi quod odit similique totam harum. Est eum magnam illum voluptate rem mollitia soluta facere enim minus repudiandae aliquam hic quas, nobis neque natus doloremque minima atque non vitae nam accusantium libero? Quisquam dolorum accusamus reiciendis nam magni saepe mollitia molestias? Dicta repellat praesentium corrupti iste delectus doloremque reprehenderit. Tenetur, unde veritatis nihil dolorem mollitia iure id, dolores maxime quos repellat esse odio magnam debitis accusamus obcaecati porro laudantium corrupti eveniet ad consectetur? Necessitatibus error repudiandae unde illo. Dolorem, commodi facere molestias tempore aut quas debitis excepturi voluptate reiciendis quis quibusdam odio consequuntur aspernatur ullam sequi earum numquam reprehenderit blanditiis minima ut quia placeat explicabo? Quidem enim culpa quam a dicta beatae quasi?",
                    date: "21/10/2020"
                },
                 {
                    title:"Lorem ipsum dolor sit amet consectetur adipisicing elit. Sapiente consectetur perspiciatis eum fugit ut rem? Fugit eveniet unde tempore, nihil autem sequi nobis perferendis, ullam debitis assumenda impedit voluptatum soluta.",
                    content:"Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ipsam ipsum corrupti nesciunt quis, natus saepe repellendus enim optio animi? Harum assumenda eum fuga ducimus, minus itaque atque quisquam unde voluptatem rerum odio nihil autem deserunt in at facere ea. Doloremque sapiente qui dolorum soluta provident consectetur mollitia consequatur magni at expedita explicabo est, eos ipsa odio debitis eius! Quo exercitationem ut autem beatae aliquam qui repudiandae dolor, maxime architecto sit iste perferendis, est, sed aspernatur repellat? Dolore, natus. Quis magnam voluptate sit consequuntur eum labore repellendus, in quia illum dignissimos eligendi culpa natus quas voluptates voluptatibus iure corporis non libero maiores! Dolores impedit dolorum consequuntur, molestias alias tempore? Quae recusandae itaque aspernatur sunt repellendus eaque, nesciunt laboriosam debitis a omnis explicabo commodi tempore consequatur corrupti! Minima ratione maiores necessitatibus fugiat, numquam alias recusandae dolores error consectetur et animi quod odit similique totam harum. Est eum magnam illum voluptate rem mollitia soluta facere enim minus repudiandae aliquam hic quas, nobis neque natus doloremque minima atque non vitae nam accusantium libero? Quisquam dolorum accusamus reiciendis nam magni saepe mollitia molestias? Dicta repellat praesentium corrupti iste delectus doloremque reprehenderit. Tenetur, unde veritatis nihil dolorem mollitia iure id, dolores maxime quos repellat esse odio magnam debitis accusamus obcaecati porro laudantium corrupti eveniet ad consectetur? Necessitatibus error repudiandae unde illo. Dolorem, commodi facere molestias tempore aut quas debitis excepturi voluptate reiciendis quis quibusdam odio consequuntur aspernatur ullam sequi earum numquam reprehenderit blanditiis minima ut quia placeat explicabo? Quidem enim culpa quam a dicta beatae quasi?",
                    date: "21/10/2020"
                },
                 {
                    title:"Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quam culpa cupiditate dolor perferendis laudantium exercitationem!",
                    content:"Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ipsam ipsum corrupti nesciunt quis, natus saepe repellendus enim optio animi? Harum assumenda eum fuga ducimus, minus itaque atque quisquam unde voluptatem rerum odio nihil autem deserunt in at facere ea. Doloremque sapiente qui dolorum soluta provident consectetur mollitia consequatur magni at expedita explicabo est, eos ipsa odio debitis eius! Quo exercitationem ut autem beatae aliquam qui repudiandae dolor, maxime architecto sit iste perferendis, est, sed aspernatur repellat? Dolore, natus. Quis magnam voluptate sit consequuntur eum labore repellendus, in quia illum dignissimos eligendi culpa natus quas voluptates voluptatibus iure corporis non libero maiores! Dolores impedit dolorum consequuntur, molestias alias tempore? Quae recusandae itaque aspernatur sunt repellendus eaque, nesciunt laboriosam debitis a omnis explicabo commodi tempore consequatur corrupti! Minima ratione maiores necessitatibus fugiat, numquam alias recusandae dolores error consectetur et animi quod odit similique totam harum. Est eum magnam illum voluptate rem mollitia soluta facere enim minus repudiandae aliquam hic quas, nobis neque natus doloremque minima atque non vitae nam accusantium libero? Quisquam dolorum accusamus reiciendis nam magni saepe mollitia molestias? Dicta repellat praesentium corrupti iste delectus doloremque reprehenderit. Tenetur, unde veritatis nihil dolorem mollitia iure id, dolores maxime quos repellat esse odio magnam debitis accusamus obcaecati porro laudantium corrupti eveniet ad consectetur? Necessitatibus error repudiandae unde illo. Dolorem, commodi facere molestias tempore aut quas debitis excepturi voluptate reiciendis quis quibusdam odio consequuntur aspernatur ullam sequi earum numquam reprehenderit blanditiis minima ut quia placeat explicabo? Quidem enim culpa quam a dicta beatae quasi?",
                    date: "21/10/2020"
                },
                {
                    title:"Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quam culpa cupiditate dolor perferendis laudantium exercitationem!",
                    content:"Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ipsam ipsum corrupti nesciunt quis, natus saepe repellendus enim optio animi? Harum assumenda eum fuga ducimus, minus itaque atque quisquam unde voluptatem rerum odio nihil autem deserunt in at facere ea. Doloremque sapiente qui dolorum soluta provident consectetur mollitia consequatur magni at expedita explicabo est, eos ipsa odio debitis eius! Quo exercitationem ut autem beatae aliquam qui repudiandae dolor, maxime architecto sit iste perferendis, est, sed aspernatur repellat? Dolore, natus. Quis magnam voluptate sit consequuntur eum labore repellendus, in quia illum dignissimos eligendi culpa natus quas voluptates voluptatibus iure corporis non libero maiores! Dolores impedit dolorum consequuntur, molestias alias tempore? Quae recusandae itaque aspernatur sunt repellendus eaque, nesciunt laboriosam debitis a omnis explicabo commodi tempore consequatur corrupti! Minima ratione maiores necessitatibus fugiat, numquam alias recusandae dolores error consectetur et animi quod odit similique totam harum. Est eum magnam illum voluptate rem mollitia soluta facere enim minus repudiandae aliquam hic quas, nobis neque natus doloremque minima atque non vitae nam accusantium libero? Quisquam dolorum accusamus reiciendis nam magni saepe mollitia molestias? Dicta repellat praesentium corrupti iste delectus doloremque reprehenderit. Tenetur, unde veritatis nihil dolorem mollitia iure id, dolores maxime quos repellat esse odio magnam debitis accusamus obcaecati porro laudantium corrupti eveniet ad consectetur? Necessitatibus error repudiandae unde illo. Dolorem, commodi facere molestias tempore aut quas debitis excepturi voluptate reiciendis quis quibusdam odio consequuntur aspernatur ullam sequi earum numquam reprehenderit blanditiis minima ut quia placeat explicabo? Quidem enim culpa quam a dicta beatae quasi?",
                    date: "21/10/2020"
                },
                {
                    title:"Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quam culpa cupiditate dolor perferendis laudantium exercitationem!",
                    content:"Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ipsam ipsum corrupti nesciunt quis, natus saepe repellendus enim optio animi? Harum assumenda eum fuga ducimus, minus itaque atque quisquam unde voluptatem rerum odio nihil autem deserunt in at facere ea. Doloremque sapiente qui dolorum soluta provident consectetur mollitia consequatur magni at expedita explicabo est, eos ipsa odio debitis eius! Quo exercitationem ut autem beatae aliquam qui repudiandae dolor, maxime architecto sit iste perferendis, est, sed aspernatur repellat? Dolore, natus. Quis magnam voluptate sit consequuntur eum labore repellendus, in quia illum dignissimos eligendi culpa natus quas voluptates voluptatibus iure corporis non libero maiores! Dolores impedit dolorum consequuntur, molestias alias tempore? Quae recusandae itaque aspernatur sunt repellendus eaque, nesciunt laboriosam debitis a omnis explicabo commodi tempore consequatur corrupti! Minima ratione maiores necessitatibus fugiat, numquam alias recusandae dolores error consectetur et animi quod odit similique totam harum. Est eum magnam illum voluptate rem mollitia soluta facere enim minus repudiandae aliquam hic quas, nobis neque natus doloremque minima atque non vitae nam accusantium libero? Quisquam dolorum accusamus reiciendis nam magni saepe mollitia molestias? Dicta repellat praesentium corrupti iste delectus doloremque reprehenderit. Tenetur, unde veritatis nihil dolorem mollitia iure id, dolores maxime quos repellat esse odio magnam debitis accusamus obcaecati porro laudantium corrupti eveniet ad consectetur? Necessitatibus error repudiandae unde illo. Dolorem, commodi facere molestias tempore aut quas debitis excepturi voluptate reiciendis quis quibusdam odio consequuntur aspernatur ullam sequi earum numquam reprehenderit blanditiis minima ut quia placeat explicabo? Quidem enim culpa quam a dicta beatae quasi?",
                    date: "21/10/2020"
                },
                {
                    title:"Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptas voluptatibus sapiente aperiam quas excepturi fugiat delectus, doloribus, est saepe officia voluptatem nobis iste nam, temporibus corrupti consequatur corporis facere dolor.",
                    content:"Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ipsam ipsum corrupti nesciunt quis, natus saepe repellendus enim optio animi? Harum assumenda eum fuga ducimus, minus itaque atque quisquam unde voluptatem rerum odio nihil autem deserunt in at facere ea. Doloremque sapiente qui dolorum soluta provident consectetur mollitia consequatur magni at expedita explicabo est, eos ipsa odio debitis eius! Quo exercitationem ut autem beatae aliquam qui repudiandae dolor, maxime architecto sit iste perferendis, est, sed aspernatur repellat? Dolore, natus. Quis magnam voluptate sit consequuntur eum labore repellendus, in quia illum dignissimos eligendi culpa natus quas voluptates voluptatibus iure corporis non libero maiores! Dolores impedit dolorum consequuntur, molestias alias tempore? Quae recusandae itaque aspernatur sunt repellendus eaque, nesciunt laboriosam debitis a omnis explicabo commodi tempore consequatur corrupti! Minima ratione maiores necessitatibus fugiat, numquam alias recusandae dolores error consectetur et animi quod odit similique totam harum. Est eum magnam illum voluptate rem mollitia soluta facere enim minus repudiandae aliquam hic quas, nobis neque natus doloremque minima atque non vitae nam accusantium libero? Quisquam dolorum accusamus reiciendis nam magni saepe mollitia molestias? Dicta repellat praesentium corrupti iste delectus doloremque reprehenderit. Tenetur, unde veritatis nihil dolorem mollitia iure id, dolores maxime quos repellat esse odio magnam debitis accusamus obcaecati porro laudantium corrupti eveniet ad consectetur? Necessitatibus error repudiandae unde illo. Dolorem, commodi facere molestias tempore aut quas debitis excepturi voluptate reiciendis quis quibusdam odio consequuntur aspernatur ullam sequi earum numquam reprehenderit blanditiis minima ut quia placeat explicabo? Quidem enim culpa quam a dicta beatae quasi?",
                    date: "21/10/2020"
                },
            ],
        }
    },
    filters: {
        truncate: function (text, length) {
            return text.length > length ? text.substring(0, length) + "..." : text;
        }
    }
}
</script>

<style scoped>
a {
    text-decoration: none;
    color: black;
}

.main {
    width: 90%;
    margin:0px auto;
}

.banner {
    background-image: url("../assets/background2.jpg");
    background-position: center center;
    background-repeat: no-repeat;
    background-size:cover;
    height: 400px;
}

.banner p {
    width: 700px;
    padding-top:70px;
    color: white;
    font-size: 2em;
}

.context {
    margin-top: 25px;
    border: 1px gray solid;
    margin-bottom: 25px;
}

.header {
    display: flex;
    justify-content: space-between;
    border-bottom: 1px gray solid;
}

.haberler {
    width: inherit;
    text-align: left;
    padding: 20px;
}

.haberler h3{
    color: red;
    margin-bottom: 10px;
}

.haberler ul li {
    border-bottom: 1px solid gray;
    padding: 10px;
}

.title {
    font-weight: bold;
}

.singleHaber {
    cursor: pointer;
}

.content {
    font-size: 14px;
    color: gray;
}

ul {
    list-style: none;
}

.tum {
    cursor: pointer;
}


@media only screen and (max-width: 820px) {
  .main {
    width: 100%;
  }

  .habeler {
      width: 100%;
  }

  .banner p {
      padding: 5px;
      width: 100%;
      color: white;
      font-weight: bold;
  }
}


</style>