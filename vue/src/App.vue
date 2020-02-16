<template>
  <div id="app">
    <b-container>
      <banner />
      <upload-form
        v-if="!finishedBeatUrl"
        @done="finishedBeatUrl = $event"
      />
      <audio-player
        v-else
        :src="finishedBeatUrl"
        @back="finishedBeatUrl = ''"
      />
    </b-container>
  </div>
</template>

<script>
import Banner from './components/Banner.vue';
import UploadForm from './components/UploadForm.vue';
import AudioPlayer from './components/AudioPlayer.vue';

export default {
  components: {
    Banner,
    UploadForm,
    AudioPlayer,
  },
  data() {
    return {
      finishedBeatUrl: '',
    };
  },
};
</script>
