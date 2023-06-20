<template>



    <div id="contenedor_formulario">


            <div id="contenedor_inputs">
                <input id="input_crear" type="text" v-model="titulo" @keyup:enter="crearTarea" placeholder="Ingresa el titulo">
                <input id="input_crear"  type="text" v-model="descripcion" placeholder="Ingresa la descripcion">
            </div>
           

            <div id="contenedor_combo_box">
                <select id="combobox" v-model="prioridad">
                <option>Alta</option>
                <option>Media</option>
                <option>Baja</option>
                </select>
            </div>
       
            <div id="contenedor_boton">
                <button id="boton_crear_tarea" @click.prevent="crearTarea" >Crear Tarea</button>
            </div>

  

        
    </div>
  
 


</template>





<script>


export default{
    data(){
        return{
            titulo : '',
            descripcion : '',
            prioridad :'',
            nombre_usuario : '',
        }
    },
    methods: {                              //crear_tarea
        async crearTarea(){
            const tarea = {
                titulo: this.titulo,
                descripcion: this.descripcion,
                prioridad: this.prioridad,
                nombre_usuario: this.$store.state.nombreUsuario,  // indentificar el nombre_usuario y agregarlo al campo de nombre de usuario
            };
            try{
                const respuesta = await this.$store.dispatch('crearTarea', tarea);
                console.log(respuesta);
            } catch(error){
                console.error(error);
            }
        },
        
    }



}


</script>




<style scoped>
#contenedor_formulario{
    width: 20%;
    height: auto;
    background: rgba(207, 23, 198, 0);
    display: flex;
    justify-content: center;
    flex-direction: column;
    gap: 10px;
    padding: 20px;
}

#contenedor_inputs{
    display: flex;
    flex-direction: column;
    gap: 10px;
}

#contenedor_combo_box{
    display: flex;
    justify-items: flex-start;

 
}


#contenedor_boton{
    display: flex;
    justify-content: flex-start;
    align-items: center;
}

#contenedor_boton #boton_crear_tarea{
    padding: 11px;
    outline: 0;
    border: 0;
    color: rgb(255, 255, 255);
    background: green;
    border-radius: 10px;
    cursor: pointer;
    width:100px;
}


#contenedor_inputs input{
    box-sizing: border-box;
    background-color: #546e7a21;
    border: 1px solid #546E7A;
    border-radius: 3px;
    font-size: 1rem;
    outline: 0;
    padding: 0.8rem;
    transition: all 600ms ease;
    color: white;
    width: 300px;
}

input::placeholder{
    color: white;
}
form input:focus,
input:active {
    background: rgba(255, 255, 255, 0.932);
    color: #ffffff;
}
#contenedor_combo_box select, option{
    padding: 2px;
    color: rgb(0, 0, 0);
}







</style>