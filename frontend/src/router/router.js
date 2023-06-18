import { createRouter, createWebHistory } from 'vue-router';   // Librería de vue router importación





import InicioComponent from '@/views/inicioComponent.vue';      // Importación del componente de inicio que está en la sección views llamada InicioComponent.vue
import registrarComponent from '@/views/auth/RegistrarComponent.vue';
import LoginComponent from '@/views/auth/LoginComponent.vue'
import PanelComponent from '@/views/PanelComponent.vue'

const routes = [   //Se crea una constante de rutas o routes,  donde adentro de las llaves contiene un array dónde contiene las rutas de cada componente ala que le llamamos.
  { path: '/', redirect: '/inicio' },   
  { path: '/inicio', component: InicioComponent },   
  { path: '/registrar', component: registrarComponent },
  { path: '/login', component: LoginComponent },
  { path: '/panel', component: PanelComponent, meta: { requiresAuth: true } },
];






const router = createRouter({  /* Acá definimos como enrutador en general dónde llama a routes o rutas de arriba,  y lo ejecuta dentro de la librería */
  history: createWebHistory(),
  routes
});




export default router;  
