import { createRouter, createWebHistory } from 'vue-router';   // Librería de vue router importación
import InicioComponent from '@/views/inicioComponent.vue';      // Importación del componente de inicio que está en la sección views llamada InicioComponent.vue
import CrearUsuarioComponent from '@/components/crearUsuariosComponent.vue';
import listarUsuariosComponent from '@/components/listarUsuariosComponent.vue';

const routes = [   //Se crea una constante de rutas o routes,  donde adentro de las llaves contiene un array dónde contiene las rutas de cada componente ala que le llamamos.
  { path: '/', redirect: '/inicio' },   
  { path: '/inicio', component: InicioComponent },   
  { path: '/usuarios/crear', component: CrearUsuarioComponent },
  { path: '/usuarios', component: listarUsuariosComponent },     
];






const router = createRouter({  /* Acá definimos como enrutador en general dónde llama a routes o rutas de arriba,  y lo ejecuta dentro de la librería */
  history: createWebHistory(),
  routes
});



export default router;   /* esto es simplemente exportar la configuración para usarlo en MAIN.JS que está en la esctructura del proyecto */
