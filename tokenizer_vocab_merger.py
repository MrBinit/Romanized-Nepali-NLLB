from sentencepiece import sentencepiece_model_pb2 as sp
from transformers import NllbTokenizer, AutoModelForSeq2SeqLM
from build_custom_tokenizer import SPM_PREFIX, spm

tokenizer = NllbTokenizer.from_pretrained('facebook/nllb-200-distilled-600M') 
sp_trained = spm.SentencePieceProcessor(model_file=f'{SPM_PREFIX}.model')
added_spm = sp.ModelProto()
added_spm.ParseFromString(sp_trained.serialized_model_proto())
old_spm = sp.ModelProto()
old_spm.ParseFromString(tokenizer.sp_model.serialized_model_proto())

nllb_tokens_set = {p.piece for p in old_spm.pieces}
prev_min_score = old_spm.pieces[-1].score
for p in added_spm.pieces:
  piece = p.piece

  if p.type !=1:
    continue
  if piece not in nllb_tokens_set:
    new_p = sp.ModelProto().SentencePiece()
    new_p.piece = piece
    new_p.score = prev_min_score + prev_min_score
    old_spm.pieces.append(new_p)

NEW_SPM_NAME = 'spm_nllb_npi_roman.model'
with open(NEW_SPM_NAME, 'wb') as f:
  f.write(old_spm.SerializeToString())
