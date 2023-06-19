import { createStore } from 'vuex';
import axios from 'axios';


const store = createStore({

  state: {
    estaAutenticado: false,
    usuarios: [],
    tareas: [],
  },



  mutations: {
    agregarUsuario(state, usuario) {
      //console.log('usuario agregado desde index.js')
      state.usuarios.push(usuario);
    },
    agregarTarea(state, tarea){
      state.tareas.push(tarea)
    },
    establecerAutenticado(state, estaAutenticado) {
      console.log('Estado de autenticación actualizado:', estaAutenticado);
      state.estaAutenticado = estaAutenticado;
    },
  },



  actions:{
      async crearUsuario({ commit }, usuario) {  
        try {
          const response = await axios.post('http://localhost:5000/crear_usuario', usuario);
          commit('agregarUsuario', response.data.respuesta);
          return response.data.respuesta;
          
        } catch (error) {
          console.error('Error al crear el usuario:', error);
          throw error;
        }
      },
    
     async crearTarea({ commit }, tarea){
      try{
        const response = await axios.post('http://localhost:5000/crear_tarea', tarea);
        commit('agregarTarea', response.data.respuesta);
        console.log(response.data)
        return response.data.respuesta;

      } catch(error){
        console.error('error al crear la tarea:', error)
        throw error;
        
      }

     } 
   



  },




});






export default store;

