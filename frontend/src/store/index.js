import { createStore } from 'vuex';
import axios from 'axios';



const store = createStore({

      state: {
        estaAutenticado: false,
        nombreUsuario: '',
        usuarios: [],
        tareas: [],
        verTarea:[],
      },



  mutations: {
    agregarUsuario(state, usuario) {
      //console.log('usuario agregado desde index.js')
      state.usuarios.push(usuario);
    },
    agregarTarea(state, tarea){
      console.log('agregando tarea:', tarea);
      state.tareas.push(tarea)
    },
    verTarea(state, tarea){
      console.log('función verTarea:', tarea);
      state.tareas.push(tarea)
    },
    establecerAutenticado(state, estaAutenticado) {
      //console.log('estado de autenticación actualizado:', estaAutenticado);
      state.estaAutenticado = estaAutenticado;
    },
    establecerNombreUsuario(state, nombreUsuario) {
      state.nombreUsuario = nombreUsuario;     
    },

  },



    actions:{
      /*______________________________________*/
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
      /*______________________________________*/
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
      },
      /*______________________________________*/
        async listarTarea({ commit }, nombreUsuario){
          try{
            const response = await axios.post('http://localhost:5000/listar_tareas', nombreUsuario);
            commit('verTarea', response.data.respuesta);
            console.log('funcion asincrona listarTarea', response.data)
            return response.data.respuesta;
          } catch(error){
            console.error('error al leer la tarea:',error)
            throw error;
          }
      },
    }   
});






export default store;

