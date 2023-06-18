import { createStore } from 'vuex';
import axios from 'axios';


const store = createStore({

  state: {
    estaAutenticado: false,
    usuarios: [],
  },



  mutations: {
    agregarUsuario(state, usuario) {
      state.usuarios.push(usuario);
    },
    establecerAutenticado(state, estaAutenticado) {
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

