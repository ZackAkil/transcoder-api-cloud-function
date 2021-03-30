from google.cloud.video import transcoder

OUTPUT_BUCKET = 'gs://YOUR OUTPUT BUCKET/'
PROJECT_ID = '123456789'
LOCATION = 'europe-west1'

parent_location = f"projects/{project_id}/locations/{location}"

transcoder_client = transcoder.TranscoderServiceClient()

def transcode_video(event, context):
  
    print(event)

    gcs_uri = 'gs://' + event['bucket'] + '/' + event['name']
    just_file_name = event['name'].split('.')[0]
    
    job = transcoder.Job()
    job.input_uri = gcs_uri
    job.output_uri = OUTPUT_BUCKET + just_file_name + '/'
    job.template_id = 'preset/web-hd'

    response = transcoder_client.create_job(parent=parent_location, job=job)
    
    print(response)
    print("\nTranscoding video.")
