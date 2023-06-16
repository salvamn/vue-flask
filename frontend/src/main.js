import { createApp } from 'vue';
import App from './App.vue';                            //Importación de todo como router,store,mutations,actions,etc.  
import router from './router/router.js';

import store from './store/index.js' //lo incorporé





const app = createApp(App);     /* definimos en la constante app para tomar la creación de la aplicación */
app.use(router);  
app.use(store);          /* acá llamamos al otro archivo de router.js que está en la estructura y simplmenete lo que hace es usarlo. */
app.mount('#app');  //Acá lo monta definitamente todo.
