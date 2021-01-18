<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Plates</h1>
        <hr><br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Plate</th>
              <th scope="col">Timestamp</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="post of posts" :key="post">
              <td>{{post.plate }}</td>
              <td>{{post.timestamp }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
  export default {
    created() {
      this.getPosts();
    },
    data() {
      return {
        posts: [],
        errors: [],
        plateinput : '',
        newlyaddedplate : ''
      };
    },
    methods: {
      getPosts() {
       axios.defaults.headers.post['Access-Control-Allow-Headers'] = '*' // for POST requests
        axios
          .get("http://localhost:5000/plate")
          .then(response => (this.posts = response.data))
          .catch(error => {
            this.errors.push(error);
          });
      },
      async created() {
        const car = { plate: this.plateinput };
        axios.post("http://localhost:5000/plate", car)
        .then(response => console.log(response));
      }
    }
  };
</script>
<style>
h1 {
  text-align: left;
}
</style>



