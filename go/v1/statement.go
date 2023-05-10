/*
 * Wrapper APIs for in-toto attestation Statement layer protos.
*/

package v1

import (
	"errors"
	
	"google.golang.org/protobuf/types/known/structpb"
)

const StatementTypeUri = "https://in-toto.io/Statement/v1"

func NewStatementPb(subject []*ResourceDescriptor,
	predicateType string,
	predicate *structpb.Struct) (*Statement, error) {
	
	s := &Statement{
		Type:          StatementTypeUri,
		Subject:       subject,
		PredicateType: predicateType,
		Predicate:     predicate,
	}

	if !IsValidStatement(s) {
		return nil, errors.New("malformed Statement")
	}
	
	return s, nil
}

func IsValidStatement(s *Statement) bool {
	if s.GetType() != StatementTypeUri {
		return false
	}
	
	if s.GetSubject() == nil || len(s.GetSubject()) == 0 {
		return false
	}
	
	// check all resource descriptors in the subject
	subject := s.GetSubject()
	for _, rd := range subject {
		if !IsValidResourceDescriptor(rd) {
			return false
		}

		// v1 statements require the digest to be set in the subject
		digest := rd.GetDigest()
		if digest == nil || len(digest) == 0 {
			return false
		}
	}
	
	if s.GetPredicateType() == "" {
		return false
	}
	
	if s.GetPredicate() == nil {
		return false
	}

	return true
}
