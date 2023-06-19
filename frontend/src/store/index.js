import { createStore } from 'vuex';
import axios from 'axios';


const store = createStore({

  state: {
    estaAutenticado: false,
    usuarios: [],
  },



  mutations: {
    agregarUsuario(state, usuario) {
      //console.log('usuario agregado desde index.js')
      state.usuarios.push(usuario);
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
      }
  },




});






export default store;

