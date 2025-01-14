import sentencepiece as spm
import yaml 

def load_config(config_path="config.yaml"):
    with open(config_path, "r") as f:
        return yaml.safe_load(f)
    
config = load_config()
text_file = config["text_file"]

SPM_PREFIX = 'npi_roman'
print(f"Text file path: {text_file}")

spm.SentencePieceTrainer.train(
    input = text_file,
    model_prefix = SPM_PREFIX,
    vocab_size = 32000,
    character_coverage=1, 
    shuffle_input_sentence= True,
    num_threads = 16, 
    bos_id = 0,
    eos_id = 2,
    pad_id = 1,
    unk_id = 3,
    add_dummy_prefix = True,
    train_extremely_large_corpus = False,
    max_sentencepiece_length = 50,
    max_sentence_length = 4192*4

)