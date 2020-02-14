<template>
  <div id="app">
    <b-container>
      <banner />
      <upload-form />
    </b-container>
  </div>
</template>

<script>
import Banner from './components/Banner.vue';
import UploadForm from './components/UploadForm.vue';

export default {
  components: {
    Banner,
    UploadForm,
  },
};
</script>
