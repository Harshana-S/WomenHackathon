<template>
<html>
<head>
    
</head>
<body>
<div>
<v-stepper ref="stepper" :steps="5" v-model="step"></v-stepper>

<div v-if="step === 1">
    <section id="selectDestination">
    <!-- <h3>Select Destination</h3> -->
    <div class="container"></div>
    <div class="searchText">
    <img class="logo" src="../assets/city_gal.png" >
    <form id="destination">
    <input id="searchbar" placeholder="Enter your search destination" v-model="destination"/>
    {{destination}}
    </form>
    <div class="buttons">
    <button id="button_enter" v-scroll-to="'#down'">Enter</button>
    </div> 
    </div>
    <br/>
   
    <button id="cont" class="buttond" type="button" @click="$refs.stepper.next()">Continue</button>
    

    </section>
</div>
<div v-if="step === 2">
    <section id="ChoosePlaces">
        <h3>Choose Places</h3>
        <div class="icons">
        <heart-icon />
        </div>
        <h5> Double Tap To Like</h5>
        <div class="card-row">
            <div class="card"
            @mouseover="hoverCard(0)"
            @mouseout="hoverCard(-1)" @dblclick="handler(0)">
                <img class="card-image" src="../assets/amusement.png">
                    <div v-if="show[0]">
                        <transition name="bounce">
                            <div class="likedIcons icons">
                                <heart-icon />
                            </div>
                        </transition>
                    </div>
                    <div class="card-footer">
                        <h4 class="card-title">Amusement Parks</h4>
                    </div>
            </div>
            <div class="card"
            @mouseover="hoverCard(1)"
            @mouseout="hoverCard(-1)" @dblclick="handler(1)">
                <img class="card-image" :class="{'selected': isSelected(1)}" src="../assets/bar.png">
                    <div v-if="show[1]">
                        <transition name="bounce">
                            <div class="likedIcons icons">
                                <heart-icon />
                            </div>
                        </transition>
                    </div>
                    <div class="card-footer">
                        <h4 class="card-title">Bars</h4>
                    </div>
            </div>
            <div class="card"
            @mouseover="hoverCard(2)"
            @mouseout="hoverCard(-1)" @dblclick="handler(2)">
                <img class="card-image" src="../assets/art_museum.png">
                    <div v-if="show[2]">
                        <transition name="bounce">
                            <div class="likedIcons icons">
                                <heart-icon />
                            </div>
                        </transition>
                    </div>
                    <div class="card-footer">
                        <h4 class="card-title">Art Galleries</h4>
                    </div>
            </div>
            <div class="card"
            @mouseover="hoverCard(3)"
            @mouseout="hoverCard(-1)" @dblclick="handler(3)">
                <img class="card-image" src="../assets/restaurants.png">
                    <div v-if="show[3]">
                        <transition name="bounce">
                            <div class="likedIcons icons">
                                <heart-icon />
                            </div>
                        </transition>
                    </div>
                    <div class="card-footer">
                        <h4 class="card-title">Hotels and Restaurants</h4>
                    </div>
            </div>
        </div>
        <div class="card-row">
            <div class="card"
            @mouseover="hoverCard(4)"
            @mouseout="hoverCard(-1)" @dblclick="handler(4)">
                <img class="card-image" :class="{'selected': isSelected(4)}" src="../assets/govt_building.png">
                    <div v-if="show[4]">
                        <transition name="bounce">
                            <div class="likedIcons icons">
                                <heart-icon />
                            </div>
                        </transition>
                    </div>
                    <div class="card-footer">
                        <h4 class="card-title">Monuments</h4>
                    </div>
            </div>
            <div class="card"
            @mouseover="hoverCard(5)"
            @mouseout="hoverCard(-1)" @dblclick="handler(5)">
                <img class="card-image" src="../assets/museum.png">
                    <div v-if="show[5]">
                        <transition name="bounce">
                            <div class="likedIcons icons">
                                <heart-icon />
                            </div>
                        </transition>
                    </div>
                    <div class="card-footer">
                        <h4 class="card-title">Museums</h4>
                    </div>
            </div>
            <div class="card"
            @mouseover="hoverCard(6)"
            @mouseout="hoverCard(-1)" @dblclick="handler(6)">
                <img class="card-image" :class="{'selected': isSelected(6)}" src="../assets/parks.png">
                    <div v-if="show[6]">
                        <transition name="bounce">
                            <div class="likedIcons icons">
                                <heart-icon />
                            </div>
                        </transition>
                    </div>
                    <div class="card-footer">
                        <h4 class="card-title">Parks and Lakes</h4>
                    </div>
            </div>
            <div class="card"
            @mouseover="hoverCard(7)"
            @mouseout="hoverCard(-1)" @dblclick="handler(7)">
                <img class="card-image" :class="{'selected': isSelected(7)}" src="../assets/worship.png">
                    <div v-if="show[7]">
                        <transition name="bounce">
                            <div class="likedIcons icons">
                                <heart-icon />
                            </div>
                        </transition>
                    </div>
                    <div class="card-footer">
                        <h4 class="card-title">Places of Worship</h4>
                    </div>
            </div>

        </div>
        <div class="card-row">
            <div class="card" 
            @mouseover="hoverCard(8)"
            @mouseout="hoverCard(-1)" @dblclick="handler(8)">
            <img class="card-image" :class="{'selected': isSelected(8)}" src="../assets/mall.png">
                    <div v-if="show[8]">
                        <transition name="bounce">
                            <div class="likedIcons icons">
                                <heart-icon />
                            </div>
                        </transition>
                    </div>
                <div class="card-footer">
                    <h4 class="card-title">Shopping and Bazaar</h4>
                </div>  
            </div>

            <div class="card"
            @mouseover="hoverCard(9)"
            @mouseout="hoverCard(-1)" @dblclick="handler(9)">
                <img class="card-image" src="../assets/streetfood.png">
                    <div v-if="show[9]">
                        <transition name="bounce">
                            <div class="likedIcons icons">
                                <heart-icon />
                            </div>
                        </transition>
                    </div>
                    <div class="card-footer">
                        <h4 class="card-title">Street Food</h4>
                    </div>
            </div>

            <div class="card"
            @mouseover="hoverCard(10)"
            @mouseout="hoverCard(-1)" @dblclick="handler(10)">
                <img class="card-image" src="../assets/wildlife.png">
                    <div v-if="show[10]">
                        <transition name="bounce">
                            <div class="likedIcons icons">
                                <heart-icon />
                            </div>
                        </transition>
                    </div>
                    <div class="card-footer">
                        <h4 class="card-title">Wildlife</h4>
                    </div>
            </div>
        </div>
        <div class="switchButtons">
            <button @click="$refs.stepper.previous()">Back</button>
            <button @click="$refs.stepper.next()">Next</button>
        </div>
    </section>
</div>
<div v-if="step === 3">
    <section id="GeneratePlaces">
<button @click="getRandom">Generate Places</button>
    <div class="elements">
    <div class="parent" v-for="(item, index) in result" :key="index">{{item.Feature}}
    <div class="child" v-for="(data,index) in item.Data" :key="index">
        <button class="child_button" v-on:click="appendPlace(data)">{{data.Place}}</button>
    </div>
    </div>
    </div>
    <!-- <p>{{randomNumber}}</p>
    <p>{{number}}</p> -->
    <div class="swichButtons">
        <button @click="$refs.stepper.next()">Next</button>
        <button @click="$refs.stepper.previous()">Back</button>
    </div>
    </section>
</div>
<div v-if="step === 4">
    <div>
        <l-map :zoom="zoom" :center="center" style="height: 100vh; width: 100vw;">
        <l-tileLayer :url="url" :attribution="attribution"></l-tileLayer>
        <l-marker 
        v-for="(marker,index) in markers" :key="index"
        :lat-lng=marker></l-marker>       
        </l-map>
    </div>
    <div class="switchButtons">
        <button @click="$refs.stepper.previous()">Back</button>
        <button @click="$refs.stepper.next()">Next</button>
    </div>
</div>
<div v-if="step === 5">
    <section id="rating">
    <div class="place-star-pair">Places you have visited:
    <div class="place" v-for="(item,index) in visited_places" :key="index">{{item}}
    <div class="star"><star-rating v-bind:star-size="25" :glow="4"></star-rating></div>
    </div>
    </div>
    <div class="switchButtons">
        <button @click="$refs.stepper.previous()">Back</button>
    </div>
    </section>
</div>
</div>
</body>
</html>
</template>


<script>
/* eslint-disable no-new */
// const send={
//   'userid':'15362',
//   'places':[1,0,0,0,0,0,0,0,0,1,1]
// }
const cards= [
            'Amusement_Parks', 'Bars', 'Galleries', 'Hotels_and_Restaurants', 'Monuments',
            'Museums', 'Parks_and_Lakes', 'Places_of_Worship', 'Shopping_and_bazaar',
            'Street_food','Wildlife'
]
var show=[
    false,false,false,
    false,false,false,
    false,false,false,
    false,false
]

var places=[
    0,0,0,
    0,0,0,
    0,0,0,
    0,0
]

var latlong=
[]


import axios from 'axios'
import { VStepper } from 'vue-stepper-component'
import Datepicker from 'vuejs-datepicker'
import moment from 'moment'
//import { mapfields } from 'vuex-map-fields'
import HeartIcon from "vue-material-design-icons/Heart.vue"
import {LMap, LTileLayer, LMarker } from 'vue2-leaflet';
import SignIn from "@/components/SignIn.vue"
import StarRating from 'vue-star-rating'

export default {
    name:"Home",
    components: {
    VStepper,
    Datepicker, 
    HeartIcon,
    LMap,
    LTileLayer,
    LMarker,
    SignIn,
    StarRating
  },
  data(){
    return {
          steps: 5,
          step: undefined,
          destination:'',
          sdate: '',
          edate:'',
          cards: cards,
          selectedCards: -1,
          places:places,
          show:show,
          map: null,
          zoom: 12,
          markers: [],
          center: {},
          url: 'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
          attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
          randomNumber: 0,
          number: 0,
          result:[],
          visited_places:[]
          
    }
  },
  methods:{
       hoverCard(selectedIndex) {
            this.selectedCard = selectedIndex
      },
      isSelected(cardIndex) {
        return this.selectedCard === cardIndex;
      },
      addPlace(cardIndex){
          places[cardIndex]=1;
          //this.places.push(this.cards[cardIndex])
          console.log(this.cards[cardIndex]);
          console.log(places);
      },
      invertShow(arg){
       this.$set(this.show, arg, true)
       console.log(this.show[arg]);
       //alert(this.show[arg])
      },
      handler:function(arg){
          this.addPlace(arg);
          this.invertShow(arg)
      },
      appendPlace:function(arg){
          this.markers.push(arg.LatLng);
          this.center=this.markers[0];
          this.visited_places.push(arg.Place);
      },
      getRandom(){
          this.result = this.getRandomFromBackend()
      },
      getRandomFromBackend(){
          const path= 'http://127.0.0.1:5000/api/random'
          const send={
            'userid':'15362',
            'places':this.places
                     }
          axios.post(path,send)
          .then(response=>{
          this.result=response.data.Info
        //   this.number=response.data.number
      })
      .catch(error =>{
        console.log(error)
      })


    }
  }
}
</script>

<style scoped>
/* @import "~leaflet/dist/leaflet.css"; */
/*Lets start with the cloud formation rather*/

/*The container will also serve as the SKY*/
#selectDestination{
    width:100vw;
    height: 100vh;
    overflow-x: hidden;
}
.card-image {
  position: absolute;
  left: -9999px;
  right: -9999px;
  margin: auto;
  height: 200px;
  min-width: 200px;
}
.card-footer{
    position: absolute;
    bottom: 0;
    font-family: Helvetica;
}
.card {
  position: relative;
  background-color: rgb(255, 255, 255);
  height: 300px;
  width: 240px;
  margin-top: 0px;
  margin-left: 10px;
  margin-right: 10px;
  margin-bottom: 0px;
  overflow-x: hidden;
  box-shadow: 0px 2px 4px 0px rgba(0,0,0,0.5);
}
.card-row {
  display: flex;
  justify-content: center;
  align-items: center;  
  min-width: 780px;
  width: 100%;
  height: 500px;
}
.card {
  /* the other rules */
  transition: height 0.3s, box-shadow 0.3s;
}
.card:hover {
  height: 360px;
  box-shadow: 20px 20px 40px 0px rgba(0,0,0,0.5);
}
.card:active{
    height: 400px;
}
.card-image {
  /* the other rules */
  transition: height 0.3s, opacity 0.3s;
}
.card-image.selected {
  height: 410px;
  opacity: 0.3;
}
#stepper_header{
    flex-direction: row;
    align-items: stretch;
}
.searchText{
    margin-left: 20vw;
    margin-right: 20vw;
    height: 10vh;
    font-size: 4.5vh;
}
#searchbar{
    width: 100%;
    border-radius: 15px;
}
#textbox{
    flex-flow: row;
    align-items: center;
}
.container{
    width: auto;
    height: 100px;
}
.buttons{
    flex-direction: row;
}
button{
    margin: auto;
    margin-bottom: 50px;
    display: block;
}
#button_enter{background-color: rgb(240, 144, 144);
    color:rgb(245, 235, 235);
    align-self: center;
    
}
/* pppppppppppppppppppppppppppp */
#cont
{   background-color:rgb(240, 144, 144);
    color:rgb(245, 235, 235);
    position: absolute;
    bottom: 0px;
    right: 0px;
    height:50px;
}
button{
  padding:16px 32px;
  font-family:helvetica;
  font-size:16px;
  font-weight:100;
  color:#fff;
  background: #587286;
  border:0;
  font-weight:100;
}
button:hover{
  background: #3B5C76;
}
.switchButton{
    margin-right: 40px;
    width: auto;
    flex-direction: row;
    align-items: flex-end;
    float: right;
} 



h3{
    text-align: center;
}
h5{
    text-align: center;
}
.logo{
    /* border-radius: 60%; */
    align-self: center;
    margin:auto;
    /* margin-right: 20vw;
    margin-left: 20vw; */
    height:40vh;
    animation: run infinite;
}
@keyframes run {
    from {margin-left:-50px; }
    to{margin-right: 50px;}
}
.datesJourney{
    width: 100vw;
    margin: 5vw;
}
.icons{
    text-align: center;
    color: red;
}
.likedIcons{
    position: absolute;
    bottom: 15%;
    float: right;
}
.bounce-transition {
  display: inline-block; /* otherwise scale animation won't work */
}
.bounce-enter {
  animation: bounce-in .5s;
}
@keyframes bounce-in {
  0% {
    transform: scale(0);
  }
  50% {
    transform: scale(1.5);
  }
  100% {
    transform: scale(1);
  }
}
.switchButtons{
    display: flex;
    justify-content: center;
    align-items: center;  
}
#map {
  width: 100%;
  height: 500px;
}
#ChoosePlaces{
    background-color: #fce6e6;
}
.elements{
  display: flex;
  flex-wrap: wrap;
  margin-top: -10px;
  margin-left: -10px;

}
.parent{text-align:center;
  width: calc(25% - 10px);
  margin-left: 10px;
  margin-top: 10px;
  background-color: rgb(255, 255, 255);
  box-shadow: 0px 2px 4px 0px rgba(0,0,0,0.5);
}
.child_button{
    background-color:#ce9ec2; 
    color:beige;
    border-radius: 10px;
}
.child_button:hover{
    background-color: #dc0070;
}
.child_button:active{
    background-color: #6a3b5e;
    border-color: cornsilk;
    border-width: 3px;
}

.place-star-rating{
    display: grid;
    grid-gap: 50px;
    grid-template-columns: 1fr 1fr;
    align-self: center;
}
.place{
    margin: 5px 5px 3px 5px;
}
.star{
    margin: 3px 5px 5px 5px;
}
</style>