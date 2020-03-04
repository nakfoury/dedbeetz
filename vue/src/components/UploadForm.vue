<template>
  <b-card
    header="Create your Beat"
    :footer="isUploading ? 'Your Beat is very important to us' : ''"
  >
    <b-alert
      v-model="isFailed"
      variant="danger"
    >
      {{ errorMessage }}
    </b-alert>
    <audio-recorder
      class="mb-4"
      style="text-align: center"
      @done="onDoneRecording"
    />
    <b-form @submit.prevent="submit">
      <b-form-group>
        <b-form-file
          v-model="file"
          accept="audio/*"
          placeholder="Choose a beatbox audio file..."
          drop-placeholder="Drop beatbox here..."
          :disabled="isUploading"
          required
        />
      </b-form-group>
      <b-button
        v-if="file"
        type="submit"
        variant="primary"
        :disabled="isUploading"
      >
        <b-spinner
          v-if="isUploading"
          small
        />
        {{ isUploading ? "Processing" : "Submit" }}
      </b-button>
    </b-form>
  </b-card>
</template>

<script>
import axios from 'axios';
import AudioRecorder from './AudioRecorder.vue';

const STATUS_INITIAL = 0;
const STATUS_UPLOADING = 1;
const STATUS_SUCCESS = 2;
const STATUS_FAILED = 3;

export default {
  components: { AudioRecorder },
  data() {
    return {
      file: undefined,
      status: STATUS_INITIAL,
      errorMessage: '',
    };
  },
  computed: {
    isUploading() { return this.status === STATUS_UPLOADING; },
    isFailed() { return this.status === STATUS_FAILED; },
  },
  mounted() {
    this.status = STATUS_INITIAL;
  },
  methods: {
    onDoneRecording(file) {
      this.file = file;
      this.submit();
    },
    async submit() {
      const formData = new FormData();
      formData.append('fileToUpload', this.file);
      this.status = STATUS_UPLOADING;
      try {
        const { data } = await axios.post('/upload', formData);
        this.status = STATUS_SUCCESS;
        this.$emit('done', data);
      } catch (err) {
        this.errorMessage = err;
        this.status = STATUS_FAILED;
      }
    },
  },
};
</script>
