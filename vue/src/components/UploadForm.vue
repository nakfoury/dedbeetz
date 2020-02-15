<template>
  <b-card>
    <b-card-body>
      <b-alert
        v-model="isFailed"
        variant="danger"
      >
        {{ errorMessage }}
      </b-alert>
      <b-alert
        v-model="isSuccess"
        variant="success"
      >
        Successfully uploaded {{ file.name }}
      </b-alert>
      <b-form
        v-if="!isSuccess"
        @submit.prevent="submit"
      >
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
          type="submit"
          variant="primary"
          :disabled="isUploading"
        >
          <b-spinner
            v-if="isUploading"
            small
          />
          Submit
        </b-button>
      </b-form>
    </b-card-body>
  </b-card>
</template>

<script>
import axios from 'axios';

const STATUS_INITIAL = 0;
const STATUS_UPLOADING = 1;
const STATUS_SUCCESS = 2;
const STATUS_FAILED = 3;

export default {
  data() {
    return {
      file: [],
      status: STATUS_INITIAL,
      errorMessage: '',
    };
  },
  computed: {
    isUploading() { return this.status === STATUS_UPLOADING; },
    isSuccess() { return this.status === STATUS_SUCCESS; },
    isFailed() { return this.status === STATUS_FAILED; },
  },
  mounted() {
    this.status = STATUS_INITIAL;
  },
  methods: {
    submit() {
      const formData = new FormData();
      formData.append('fileToUpload', this.file);
      this.status = STATUS_UPLOADING;
      axios.post('/upload', formData)
        .then(() => {
          this.status = STATUS_SUCCESS;
        })
        .catch((err) => {
          this.errorMessage = err;
          this.status = STATUS_FAILED;
        });
    },
  },
};
</script>
