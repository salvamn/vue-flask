import { createApp } from 'vue';
import App from './App.vue';                            //Importación de todo como router,store,mutations,actions,etc.  
import router from './router';  


const app = createApp(App);     /* definimos en la constante app para tomar la creación de la aplicación */
app.use(router);            /* acá llamamos al otro archivo de router.js que está en la estructura y simplmenete lo que hace es usarlo. */
app.mount('#app');  //Acá lo monta definitamente todo.
